
def my_filter(elem: str):
    if "https://t.co/" in elem:
        return False
    return True

my_file = open("scrapper/hashtags_johnnydepp.txt", "r")
content_list = my_file.readlines()
content_list = filter(my_filter, content_list)
text = " ".join(content_list)

from nltk.sentiment.vader import SentimentIntensityAnalyzer
sid = SentimentIntensityAnalyzer()
ss = sid.polarity_scores(text)
for k in sorted(ss):
    print('{0}: {1}, '.format(k, ss[k]), end='')
    print()

from nltk.tokenize import sent_tokenize
tokenized_text=sent_tokenize(text)
# print(tokenized_text)

from nltk.tokenize import word_tokenize
tokenized_word=word_tokenize(text)
# print(tokenized_word)

from nltk.probability import FreqDist
fdist = FreqDist(tokenized_word)
# print(fdist.items())

# print(fdist.most_common(5))




from nltk.corpus import stopwords
stop_words=set(stopwords.words("english"))
stop_words.add(".")
stop_words.add(",")
stop_words.add('"')
stop_words.add("'")
stop_words.add("'s")
stop_words.add("``")
stop_words.add("''")
stop_words.add("#")
stop_words.add("@")
stop_words.add("!")
stop_words.add("’")
stop_words.add("?")
stop_words.add(";")
stop_words.add("amp")
stop_words.add("&")
stop_words.add("n't")
stop_words.add(":")
stop_words.add(":")
stop_words.add("...")
stop_words.add("..")
stop_words.add("“")
stop_words.add("”")
stop_words.add("-")
stop_words.add("(")
stop_words.add(")")
stop_words.add("'m")
stop_words.add("🇯🇵")
stop_words.add("💜")
stop_words.add("🎬")
# print(stop_words)

filtered_sent=[]
for w in tokenized_word:
    if w.lower() not in stop_words:
        filtered_sent.append(w)
# print("Tokenized Sentence:",tokenized_word)
# print("Filterd Sentence:",filtered_sent)


#Lexicon Normalization
#performing stemming and Lemmatization

from nltk.stem.wordnet import WordNetLemmatizer
lem = WordNetLemmatizer()



print()
print()
fdist = FreqDist(filtered_sent)
print("Wektor słów:")
# print(fdist.items())

print("10 most common words:")
print(fdist.most_common(30))
# common10vector = fdist.most_common(30)
# labelsX = [x for (x, y) in common10vector]
# labelsY = [y for (x, y) in common10vector]



# Frequency Distribution Plot
import matplotlib.pyplot as plt
fdist.plot(30,cumulative=False)
plt.show()

# plt.bar(labelsX, labelsY)
# plt.show()




# Start with loading all necessary libraries
import numpy as np
import pandas as pd
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

import matplotlib.pyplot as plt


# Create and generate a word cloud image:
wordcloud = WordCloud().generate(text)

# Display the generated image:
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
