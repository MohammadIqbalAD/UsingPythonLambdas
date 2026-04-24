import json
import logging
from food_service import FoodItemService

# Set up logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Initialise once outside the handler so warm invocations can reuse it.
service = FoodItemService()

def lambda_handler(event, context):    
    try:
        # For now, we are triggering the "Get All" functionality
        items = service.get_all_food_items()
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Successfully retrieved items',
                'data': items
            })
        }
    except Exception as e:
        logger.error(f"Error in lambda_handler: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps({'error': 'Internal Server Error'})
        }
