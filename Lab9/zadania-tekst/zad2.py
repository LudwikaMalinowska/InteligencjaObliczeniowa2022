from sklearn.feature_extraction.text import CountVectorizer

#https://www.insider.com/johnny-depp-lawyers-posed-for-pics-alpacas-amber-heard-trial-2022-5
my_file = open("alpacas.txt", "r")
content_list = my_file.readlines()
alpacas_text = " ".join(content_list)

#https://www.independent.co.uk/news/world/americas/johnny-depp-amber-heard-closing-statements-b2088903.html
closing_arguments = open("closing_arguments.txt", "r").readlines()
closing_text = " ".join(closing_arguments)

#https://www.marca.com/en/lifestyle/celebrities/2022/05/31/629665e3e2704e91128b4603.html
pirates_boat = open("pirates_boat.txt", "r").readlines()
boat_text = " ".join(pirates_boat)



from nltk.tokenize import word_tokenize
tokenized_word_alpacas=word_tokenize(alpacas_text)
tokenized_word_closing=word_tokenize(closing_text)
tokenized_word_boat=word_tokenize(boat_text)


from nltk.corpus import stopwords
stop_words=set(stopwords.words("english"))
stop_words.add(".")
stop_words.add(",")
stop_words.add('"')
stop_words.add("'")
stop_words.add("'s")
stop_words.add("``")
stop_words.add("''")
stop_words.add("?")
stop_words.add("$")
stop_words.add("£")
stop_words.add("“")
stop_words.add("’")
stop_words.add("”")
stop_words.add("‘")


filtered_sent_alpacas=[]
for w in tokenized_word_alpacas:
    if w.lower() not in stop_words:
        filtered_sent_alpacas.append(w.lower())

filtered_sent_closing=[]
for w in tokenized_word_closing:
    if w.lower() not in stop_words:
        filtered_sent_closing.append(w.lower())

filtered_sent_boat=[]
for w in tokenized_word_boat:
    if w.lower() not in stop_words:
        filtered_sent_boat.append(w.lower())

#Lexicon Normalization
#performing stemming and Lemmatization
from nltk.stem.wordnet import WordNetLemmatizer
lem = WordNetLemmatizer()

lemmed_alpacas = []
for w in filtered_sent_alpacas:
    word = lem.lemmatize(w)
    lemmed_alpacas.append(word)

lemmed_closing = []
for w in filtered_sent_closing:
    word = lem.lemmatize(w)
    lemmed_closing.append(word)

lemmed_boat = []
for w in filtered_sent_boat:
    word = lem.lemmatize(w)
    lemmed_boat.append(word)


from sklearn.feature_extraction.text import CountVectorizer

alpacas_text = " ".join(lemmed_alpacas)
closing_text = " ".join(lemmed_closing)
boat_text = " ".join(lemmed_boat)

articles = [alpacas_text, closing_text, boat_text]
vectorizer = CountVectorizer(lowercase=True)
text_counts= vectorizer.fit_transform(articles)
print(text_counts.toarray())
# print(text_counts)


from nltk.probability import FreqDist
print()
print()
fdist = FreqDist(lemmed_closing)
print("Wektor słów:")
print(fdist.items())
print("10 most common words:")
print(fdist.most_common(10))


print("\n\nTFiD")
from sklearn.feature_extraction.text import TfidfVectorizer
tf=TfidfVectorizer()
text_tf= tf.fit_transform(articles)
print(text_tf.toarray())

from scipy import spatial
alpaca_closing_diff = 1 - spatial.distance.cosine(text_counts.toarray()[0], text_counts.toarray()[1])
alpaca_boat_diff = 1 - spatial.distance.cosine(text_counts.toarray()[0], text_counts.toarray()[2])
boat_closing_diff = 1 - spatial.distance.cosine(text_counts.toarray()[2], text_counts.toarray()[1])

print("\nalpaca_closing_diff: ", alpaca_closing_diff)
print("alpaca_boat_diff: ", alpaca_boat_diff)
print("boat_closing_diff: ", boat_closing_diff)

