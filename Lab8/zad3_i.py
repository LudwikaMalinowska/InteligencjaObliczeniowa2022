from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder

from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, multilabel_confusion_matrix
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

iris = load_iris()
# splitting into train and test datasets


datasets = train_test_split(iris.data, iris.target,
                            test_size=0.3)

train_data, test_data, train_labels, test_labels = datasets
# scaling the data

scaler = StandardScaler()

# we fit the train data
scaler.fit(train_data)

# scaling the train data
train_data = scaler.transform(train_data)
test_data = scaler.transform(test_data)

print(train_data[:3])




from numpy import array
from numpy import argmax
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
# define example
# data = train_labels
values = array(train_labels)
print(values)
# integer encode
label_encoder = LabelEncoder()
integer_encoded = label_encoder.fit_transform(values)
print(integer_encoded)
# binary encode
onehot_encoder = OneHotEncoder(sparse=False)
integer_encoded = integer_encoded.reshape(len(integer_encoded), 1)
onehot_encoded = onehot_encoder.fit_transform(integer_encoded)
print(onehot_encoded)
# invert first example
inverted = label_encoder.inverse_transform([argmax(onehot_encoded[0, :])])
print(inverted)

# Training the Model





# ----- i -----
mlp = MLPClassifier(hidden_layer_sizes=3, max_iter=5000)


# let's fit the training data to our model
mlp.fit(train_data, onehot_encoded)




predictions_train = mlp.predict(train_data)
print(accuracy_score(predictions_train, onehot_encoded))

print("predictions train")
print(predictions_train)
print("Confusion matrix: ")
print(confusion_matrix(onehot_encoded.argmax(axis=1), predictions_train.argmax(axis=1)))
# matrix = multilabel_confusion_matrix(predictions_train, onehot_encoded)
# print(matrix)

#Todo
# dla test labels też onehot encoding


# print("f: ")
# print("Ewaluacja na zbiorze testowym: ")
# predictions_test = mlp.predict(test_data)
# print(accuracy_score(predictions_test, test_labels))
# print(classification_report(predictions_test, test_labels))