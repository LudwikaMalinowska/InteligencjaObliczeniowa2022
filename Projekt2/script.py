
# importing libraries and packages
import snscrape.modules.twitter as sntwitter
import pandas as pd

# Creating list to append tweet data
tweets_list1 = []

# tweets = sntwitter.TwitterHashtagScraper("johnnydepp")

for i, tweet in enumerate(sntwitter.TwitterHashtagScraper("johnnydepp").get_items()):
    if i > 1000:  # number of tweets you want to scrape
        break
    # print(tweet)
    tweets_list1.append(
        [tweet.date, tweet.id, tweet.content, tweet.username])  # declare the attributes to be returned

tweets_df1 = pd.DataFrame(tweets_list1, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])

print(tweets_df1.head())


tweets_list2 = []

# tweets = sntwitter.TwitterHashtagScraper("johnnydepp")

for i, tweet in enumerate(sntwitter.TwitterHashtagScraper("amberheard").get_items()):
    if i > 1000:  # number of tweets you want to scrape
        break
    # print(tweet)
    tweets_list2.append(
        [tweet.date, tweet.id, tweet.content, tweet.username])  # declare the attributes to be returned

tweets_df2 = pd.DataFrame(tweets_list2, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])

print(tweets_df2.head())


tweets_list3 = []

# tweets = sntwitter.TwitterHashtagScraper("johnnydepp")

for i, tweet in enumerate(sntwitter.TwitterHashtagScraper("justiceforjohnnydepp").get_items()):
    if i > 1000:  # number of tweets you want to scrape
        break
    # print(tweet)
    tweets_list3.append(
        [tweet.date, tweet.id, tweet.content, tweet.username])  # declare the attributes to be returned

tweets_df3 = pd.DataFrame(tweets_list3, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])

print(tweets_df1.head())



tweets_list4 = []

# tweets = sntwitter.TwitterHashtagScraper("johnnydepp")

for i, tweet in enumerate(sntwitter.TwitterHashtagScraper("justiceforamberheard").get_items()):
    if i > 1000:  # number of tweets you want to scrape
        break
    # print(tweet)
    tweets_list4.append(
        [tweet.date, tweet.id, tweet.content, tweet.username])  # declare the attributes to be returned

tweets_df4 = pd.DataFrame(tweets_list4, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])

print(tweets_df4.head())



tweets_list5 = []

# tweets = sntwitter.TwitterHashtagScraper("johnnydepp")

for i, tweet in enumerate(sntwitter.TwitterHashtagScraper("amberturd").get_items()):
    if i > 1000:  # number of tweets you want to scrape
        break
    # print(tweet)
    tweets_list5.append(
        [tweet.date, tweet.id, tweet.content, tweet.username])  # declare the attributes to be returned

tweets_df5 = pd.DataFrame(tweets_list5, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])

print(tweets_df5.head())





