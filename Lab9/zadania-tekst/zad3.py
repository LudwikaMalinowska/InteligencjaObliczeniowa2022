
positive_opinion = open("opinion_positive.txt", "r").readlines()
positive_text = " ".join(positive_opinion)
negative_opinion = open("opinion_negative.txt", "r").readlines()
negative_text = " ".join(negative_opinion)

from nltk.sentiment.vader import SentimentIntensityAnalyzer


sid = SentimentIntensityAnalyzer()
# print(sentence)
ss = sid.polarity_scores(positive_text)
for k in sorted(ss):
    print('{0}: {1}, '.format(k, ss[k]), end='')
print()

sid = SentimentIntensityAnalyzer()
# print(sentence)
ss = sid.polarity_scores(negative_text)
for k in sorted(ss):
    print('{0}: {1}, '.format(k, ss[k]), end='')
print()
