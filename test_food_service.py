import os
from unittest.mock import MagicMock, patch

import pytest
from botocore.exceptions import ClientError

from food_service import FoodItemService


@pytest.fixture
def mock_env_vars():
    """
    Provide the environment variable expected by FoodItemService.
    """
    with patch.dict(os.environ, {"TABLE_NAME": "TestFoodTable"}):
        yield


@patch("boto3.resource")
def test_get_all_food_items_success(mock_boto, mock_env_vars):
    mock_table = MagicMock()
    mock_boto.return_value.Table.return_value = mock_table

    mock_table.scan.return_value = {
        "Items": [
            {"ItemID": "1", "Name": "Apple"},
            {"ItemID": "2", "Name": "Banana"},
        ]
    }

    service = FoodItemService()
    items = service.get_all_food_items()

    assert len(items) == 2
    assert items[0]["Name"] == "Apple"
    assert items[1]["Name"] == "Banana"
    mock_table.scan.assert_called_once()


@patch("boto3.resource")
def test_get_all_food_items_returns_empty_list_when_no_items(mock_boto, mock_env_vars):
    mock_table = MagicMock()
    mock_boto.return_value.Table.return_value = mock_table

    mock_table.scan.return_value = {}

    service = FoodItemService()
    items = service.get_all_food_items()

    assert items == []
    mock_table.scan.assert_called_once()


@patch("boto3.resource")
def test_get_all_food_items_raises_client_error(mock_boto, mock_env_vars):
    mock_table = MagicMock()
    mock_boto.return_value.Table.return_value = mock_table

    error_response = {
        "Error": {
            "Code": "500",
            "Message": "Internal Server Error",
        }
    }
    mock_table.scan.side_effect = ClientError(error_response, "scan")

    service = FoodItemService()

    with pytest.raises(ClientError):
        service.get_all_food_items()


def test_init_raises_if_table_name_missing():
    with patch.dict(os.environ, {}, clear=True):
        with pytest.raises(ValueError, match="TABLE_NAME environment variable is not set"):
            FoodItemService()
