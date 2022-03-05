import json
import tweepy
from config import API_KEY, API_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET, TOKEN

auth = tweepy.OAuthHandler(consumer_key=API_KEY, consumer_secret=API_KEY_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth=auth, retry_count=5)


def reply(event, context):
    body = {
        "message": "Go Serverless v3333.0! Your function executed successfully!",
        "input": event,
    }

    mentions = api.mentions_timeline()

    print(mentions)
    # for mention in mentions:
    #     print(mention)
        # print
        # mention.id, mention.author.screen_name, mention.text

    return {"statusCode": 200, "body": json.dumps(body)}
