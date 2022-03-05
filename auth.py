import tweepy
from config import ACCESS_TOKEN, ACCESS_TOKEN_SECRET, API_KEY, API_KEY_SECRET, TOKEN

auth = tweepy.OAuthHandler(
    API_KEY, API_KEY_SECRET,
    callback="oob"
)

print(auth.get_authorization_url())

verifier = input("Input PIN: ")
access_token, access_token_secret = auth.get_access_token(
    verifier
)