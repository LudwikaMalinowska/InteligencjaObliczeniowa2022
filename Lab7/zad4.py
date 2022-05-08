import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

df = pd.read_csv('diabetes.csv')

features = ['pregnant-times','glucose-concentr','blood-pressure',
            'skin-thickness','insulin','mass-index','pedigree-func','age']
all_inputs = df[features].values
all_classes = df['class'].values

(train_inputs, test_inputs, train_classes, test_classes) = \
    train_test_split(all_inputs, all_classes, train_size=0.7, random_state=1)

dtc = DecisionTreeClassifier()
dtc.fit(train_inputs, train_classes)
score = dtc.score(test_inputs, test_classes)
print(score)

from sklearn.metrics import classification_report, confusion_matrix

y_pred = dtc.predict(test_inputs)

print(confusion_matrix(test_classes, y_pred))
print(classification_report(test_classes, y_pred))