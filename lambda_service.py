import boto3
import os
import logging
from botocore.exceptions import ClientError

logger = logging.getLogger()

class FoodItemService:
    def __init__(self):
        # Fetch table name from Lambda Environment Variables
        self.table_name = os.environ.get('TABLE_NAME')
        self.dynamodb = boto3.resource('dynamodb')
        self.table = self.dynamodb.Table(self.table_name)

    def get_all_food_items(self):
        """
        Retrieves all items from the DynamoDB table and logs them to CloudWatch.
        """
        try:
            # The scan operation retrieves all items in the table
            response = self.table.scan()
            items = response.get('Items', [])
            
            # Log the items to CloudWatch
            logger.info(f"Retrieved {len(items)} items from {self.table_name}: {items}")
            
            return items
            
        except ClientError as e:
            logger.error(f"DynamoDB Error: {e.response['Error']['Message']}")
            raise e
