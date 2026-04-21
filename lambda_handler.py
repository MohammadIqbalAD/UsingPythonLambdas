import json
import logging
from lambda_service import FoodItemService

# Set up logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    service = FoodItemService()
    
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
