import pytest
import os
from unittest.mock import patch, MagicMock
from botocore.exceptions import ClientError
# Assuming your service file is named food_service.py
from food_service import FoodItemService

@pytest.fixture
def mock_env_vars():
    """Sets up the required environment variable for the class init."""
    with patch.dict(os.environ, {"TABLE_NAME": "TestFoodTable"}):
        yield

@patch('boto3.resource')
def test_get_all_food_items_success(mock_boto, mock_env_vars):
    # 1. Setup the Mock Table
    mock_table = MagicMock()
    mock_boto.return_value.Table.return_value = mock_table

    # Simulate DynamoDB returning two items
    mock_table.scan.return_value = {
        'Items': [
            {'ItemID': '1', 'Name': 'Apple'},
            {'ItemID': '2', 'Name': 'Banana'}
        ]
    }

    # 2. Execute the service method
    service = FoodItemService()
    items = service.get_all_food_items()

    # 3. Assertions
    assert len(items) == 2
    assert items[0]['Name'] == 'Apple'
    mock_table.scan.assert_called_once() # Verify the scan was actually called

@patch('boto3.resource')
def test_get_all_food_items_error(mock_boto, mock_env_vars):
    # 1. Setup Mock to raise an exception
    mock_table = MagicMock()
    mock_boto.return_value.Table.return_value = mock_table

    error_response = {'Error': {'Code': '500', 'Message': 'Internal Server Error'}}
    mock_table.scan.side_effect = ClientError(error_response, 'scan')

    # 2. Execute and Verify the exception is raised
    service = FoodItemService()
    with pytest.raises(ClientError):
        service.get_all_food_items()
