import json


def reply(event, context):
    body = {
        "message": "Go Serverless v3333.0! Your function executed successfully!",
        "input": event,
    }

    return {"statusCode": 200, "body": json.dumps(body)}
