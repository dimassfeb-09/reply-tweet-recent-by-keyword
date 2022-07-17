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

dataUserIds = ["1331650559518990336", "1205629250423779328"] # Edit this List

dataListTweetId = []

for dataUserIds in dataUserIds:
    response = client.get_users_tweets(id=dataUserIds, max_results = 10)
    tweet = response.data
    print(tweet)
    print("==========")
    
    for tweets in tweet:
        dataListTweetId.append(tweets.id)

print(dataListTweetId)

for dataTweetIds in dataListTweetId:
    response = client.create_tweet(text= "Halo", in_reply_to_tweet_id=dataTweetIds)
#     nomorke = 1
#     print(response.data)
#     print(nomorke + 1)

