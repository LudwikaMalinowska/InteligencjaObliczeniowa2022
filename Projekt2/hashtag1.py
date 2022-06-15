# importing libraries and packages
import snscrape.modules.twitter as sntwitter
import pandas as pd

# Creating list to append tweet data
tweets_list1 = []

# tweets = sntwitter.TwitterHashtagScraper("johnnydepp")

for i, tweet in enumerate(sntwitter.TwitterHashtagScraper("johnnydepp since:2021-04-10 until:2022-04-11 lang:en").get_items()):
    if i > 10000:  # number of tweets you want to scrape
        break
    # print(tweet)
    tweets_list1.append(
        [tweet.date, tweet.id, tweet.content, tweet.username])  # declare the attributes to be returned

tweets_df1 = pd.DataFrame(tweets_list1, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])

print(tweets_df1.head())



with open('hashtags_johnnydepp.txt', 'w') as the_file:
    for tweet in tweets_df1["Text"].tolist():
        # print(tweet)
        the_file.write(tweet)
        the_file.write("\n")
