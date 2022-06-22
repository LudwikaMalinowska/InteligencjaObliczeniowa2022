# importing libraries and packages
import snscrape.modules.twitter as sntwitter
import pandas as pd

# Creating list to append tweet data
tweets_list1 = []

# tweets = sntwitter.TwitterHashtagScraper("johnnydepp")
# since:2021-04-10 until:2022-04-11
for i, tweet in enumerate(sntwitter.TwitterHashtagScraper("johnnydepp since:2022-05-16 until:2022-05-23 lang:en")
                                  .get_items()):
    if i > 10000:  # number of tweets you want to scrape
        break
    # print(tweet)
    tweets_list1.append(
        [tweet.date, tweet.id, tweet.content, tweet.username])  # declare the attributes to be returned

tweets_df1 = pd.DataFrame(tweets_list1, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])

print(tweets_df1.head())




from nltk.sentiment.vader import SentimentIntensityAnalyzer
sid = SentimentIntensityAnalyzer()
for tweet in tweets_df1["Text"].head().tolist():
    ss = sid.polarity_scores(tweet)
    for k in sorted(ss):
        print('{0}: {1}, '.format(k, ss[k]), end='')
        print()

# ss = sid.polarity_scores(tweets_df1)
# for k in sorted(ss):
#     print('{0}: {1}, '.format(k, ss[k]), end='')
#     print()


with open('hashtags_johnnydepp.txt', 'w') as the_file:
    for tweet in tweets_df1["Text"].tolist():
        # print(tweet)
        the_file.write(tweet)
        the_file.write("\n")

pos_number = 0
neg_number = 0
with open('hashtags_johnnydepp_pos.txt', 'w') as the_file_pos:
    with open('hashtags_johnnydepp_neg.txt', 'w') as the_file_neg:
        for tweet in tweets_df1["Text"].tolist():
            ss = sid.polarity_scores(tweet)

            if ss["pos"] > ss["neg"]:
                the_file_pos.write(tweet)
                the_file_pos.write("\n")
                pos_number += 1
            elif ss["pos"] < ss["neg"]:
                the_file_neg.write(tweet)
                the_file_neg.write("\n")
                neg_number += 1

print(pos_number)
print(neg_number)
print(len(tweets_list1))
