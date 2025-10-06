import json
import os

# Load model at startup (global scope for efficiency)


def lambda_handler(event, context):
    """
    Lambda function for inference.
    Event should contain 'features' as a list.
    Example: {"features": [5.1, 3.5, 1.4, 0.2]}
    """
    try:
        features = event.get("features", [])
        if not features:
            return {
                "statusCode": 400,
                "body": json.dumps("No features provided")
            }

        return {
            "statusCode": 200,
            "body": json.dumps({"prediction": "Your prediction"})
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps(str(e))
        }
