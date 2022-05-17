

# bayess naiwny - zakładamy że kolumny są niezależne, a np
# od wieku zależy czy ktoś jest studentem

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

k=5
dataset = pd.read_csv('iris.csv')
names = ['sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'class']


X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 4].values


from sklearn.model_selection import train_test_split

# Split dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y,
                test_size=0.3,random_state=109) # 70% training and 30% test

#Import Gaussian Naive Bayes model
from sklearn.naive_bayes import GaussianNB

#Create a Gaussian Classifier
gnb = GaussianNB()

#Train the model using the training sets
gnb.fit(X_train, y_train)

#Predict the response for test dataset
y_pred = gnb.predict(X_test)


#Import scikit-learn metrics module for accuracy calculation
from sklearn import metrics

# Model Accuracy, how often is the classifier correct?
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))




