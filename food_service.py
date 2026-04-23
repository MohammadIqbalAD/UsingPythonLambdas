import logging
import os
from typing import Any

import boto3
from botocore.exceptions import ClientError

logger = logging.getLogger(__name__)


class FoodItemService:
    """
    Service layer for interacting with the DynamoDB food items table.

    Best practice:
    Keep AWS-specific access inside a dedicated service class rather than
    putting it directly in the Lambda handler.
    """

    def __init__(self, table: Any | None = None):
        """
        Allow an optional table to be injected for testing.

        Best practice:
        Dependency injection makes unit testing easier because tests can pass
        in a mock table instead of patching lots of AWS setup.
        """
        self.table_name = os.environ.get("TABLE_NAME")

        if table is not None:
            self.table = table
            return

        if not self.table_name:
            raise ValueError("TABLE_NAME environment variable is not set")

        # Best practice:
        # Create the DynamoDB resource only when needed and keep infrastructure
        # setup separate from business logic.
        dynamodb = boto3.resource("dynamodb")
        self.table = dynamodb.Table(self.table_name)

    def get_all_food_items(self) -> list[dict]:
        """
        Retrieve all items from the DynamoDB table.

        Note:
        Using scan() is fine for this lab because it is simple and easy to
        understand. In production, scan() is often not ideal for large tables
        because it reads the whole table and may require pagination.
        """
        try:
            response = self.table.scan()
            items = response.get("Items", [])

            # Best practice:
            # Log useful operational context, but avoid dumping large payloads
            # or sensitive data into logs unless there is a strong reason.
            logger.info(
                "Retrieved %s items from DynamoDB table %s",
                len(items),
                self.table_name,
            )

            return items

        except ClientError:
            logger.exception(
                "DynamoDB scan failed for table %s",
                self.table_name,
            )
            raise
