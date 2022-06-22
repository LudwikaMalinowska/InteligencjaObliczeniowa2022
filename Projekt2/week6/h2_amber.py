
def my_filter(elem: str):
    if "https://t.co/" in elem:
        return False
    return True

my_file = open("scrapper/hashtags_amberheard.txt", "r")
content_list = my_file.readlines()
content_list = filter(my_filter, content_list)
text = " ".join(content_list)

from nltk.tokenize import sent_tokenize
tokenized_text=sent_tokenize(text)
# print(tokenized_text)

from nltk.tokenize import word_tokenize
tokenized_word=word_tokenize(text)
# print(tokenized_word)

from nltk.probability import FreqDist
fdist = FreqDist(tokenized_word)





from nltk.corpus import stopwords
stop_words=set(stopwords.words("english"))

from Projekt2.stop_words import stop_words as my_stop_words
for word in my_stop_words:
    stop_words.add(word)

filtered_sent=[]
for w in tokenized_word:
    if w.lower() not in stop_words:
        filtered_sent.append(w)

#Lexicon Normalization
#performing stemming and Lemmatization

from nltk.stem.wordnet import WordNetLemmatizer
lem = WordNetLemmatizer()



print()
print()
fdist = FreqDist(filtered_sent)


print("10 most common words:")
print(fdist.most_common(30))



# Frequency Distribution Plot
import matplotlib.pyplot as plt
fdist.plot(30,cumulative=False)
plt.show()





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
