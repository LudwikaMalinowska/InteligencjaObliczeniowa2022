
# importing libraries and packages
import snscrape.modules.twitter as sntwitter
import pandas as pd

# Creating list to append tweet data
tweets_list1 = []

# tweets = sntwitter.TwitterHashtagScraper("johnnydepp")

for i, tweet in enumerate(sntwitter.TwitterHashtagScraper("johnnydepp").get_items()):
    if i > 100:  # number of tweets you want to scrape
        break
    # print(tweet)
    tweets_list1.append(
        [tweet.date, tweet.id, tweet.content, tweet.username])  # declare the attributes to be returned

tweets_df1 = pd.DataFrame(tweets_list1, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])

print(tweets_df1.head())



print("\n\n\n")
tweets_list2 = []

# tweets = sntwitter.TwitterHashtagScraper("johnnydepp")

for i, tweet in enumerate(sntwitter
    .TwitterHashtagScraper("johnnydepp since:2022-05-01 until:2022-05-25 near:'Gdansk' within:10km").get_items()):
    if i > 100:  # number of tweets you want to scrape
        break
    if i < 10:
        print(tweet)
    tweets_list2.append(
        [tweet.date, tweet.id, tweet.content, tweet.username])  # declare the attributes to be returned

tweets_df2 = pd.DataFrame(tweets_list2, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])

print(tweets_df2.head())




