from sklearn.datasets import load_iris

iris = load_iris()
# splitting into train and test datasets

from sklearn.model_selection import train_test_split
datasets = train_test_split(iris.data, iris.target,
                            test_size=0.3)

train_data, test_data, train_labels, test_labels = datasets
# scaling the data
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

# we fit the train data
scaler.fit(train_data)

# scaling the train data
train_data = scaler.transform(train_data)
test_data = scaler.transform(test_data)

print(train_data[:3])



# Training the Model
from sklearn.neural_network import MLPClassifier
# creating an classifier from the model:
# mlp = MLPClassifier(hidden_layer_sizes=(10, 5), max_iter=1000)



# # ----- d -----
# mlp = MLPClassifier(hidden_layer_sizes=2, max_iter=3000)


# # ----- g -----
# mlp = MLPClassifier(hidden_layer_sizes=3, max_iter=3000)

# ----- h -----
mlp = MLPClassifier(hidden_layer_sizes=(3,3), max_iter=3000)


# let's fit the training data to our model
mlp.fit(train_data, train_labels)


from sklearn.metrics import accuracy_score

predictions_train = mlp.predict(train_data)
print(accuracy_score(predictions_train, train_labels))



from sklearn.metrics import confusion_matrix

confusion_matrix(predictions_train, train_labels)


from sklearn.metrics import classification_report

print("f: ")
print("Ewaluacja na zbiorze testowym: ")
predictions_test = mlp.predict(test_data)
print(accuracy_score(predictions_test, test_labels))
print(classification_report(predictions_test, test_labels))