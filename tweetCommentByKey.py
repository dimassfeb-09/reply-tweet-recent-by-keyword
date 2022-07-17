import tweepy

BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAADUBPwEAAAAAZi%2FUlj4G2hKWijnZ%2FvkLCG0Wgy4%3DqgGplVXyncqogvY3eH194mqhgiBjJS0c4MUdOOAXM7kirePDyb"
CUSTOMER_KEY = "njSPlrcEq6Y43XHHNCAtnbImU"
CUSTOMER_SECRET = "PmLR4pxrywr4jquN9zqFw1LDKR65HWRYkc1sTTKEBuv8fqBTsR"
ACCESS_TOKEN = "1117371474183016450-JxIUmWsXIsFjqfnGJYtaDLovtTJe5n"
ACCESS_TOKEN_SECRET = "qZylrhr1lFsxGpbr2PMsTtI6MxA55waGaTUHyM2Wvig3Z"

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