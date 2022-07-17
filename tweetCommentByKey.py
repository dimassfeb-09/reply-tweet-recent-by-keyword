import tweepy

BEARER_TOKEN = ""
CUSTOMER_KEY = ""
CUSTOMER_SECRET = ""
ACCESS_TOKEN = ""
ACCESS_TOKEN_SECRET = ""

client = tweepy.Client(
    consumer_key=CUSTOMER_KEY, 
    consumer_secret=CUSTOMER_SECRET,
    access_token=ACCESS_TOKEN, 
    access_token_secret=ACCESS_TOKEN_SECRET, 
    bearer_token=BEARER_TOKEN,
)

# You can edit on below
keywordSearch = "Saran laptop dong" # Fill or Edit with keyword search what you want
yourReplyTweet = "Saran laptop nih, https://mycollection.shop/racunbydimas" # Fill or Edit with your reply what you want

# Please don't edit on below
tweetListId = []

# Run Script
response = client.search_recent_tweets(query=keywordSearch, max_results = 100) 

for searchTweet in response.data:
    tweetListId.append(searchTweet.id)

for tweetListId in tweetListId:
    response = client.create_tweet(text= yourReplyTweet, in_reply_to_tweet_id= tweetListId)
    print(response.data)
