import pandas as pd
from sklearn.model_selection import train_test_split
df = pd.read_csv("iris.csv")
(train_set, test_set) = train_test_split(df.values, train_size=0.7,
random_state=269245)

# def classify_iris(sl, sw, pl, pw):
#     if sl > 4:
#         return("Setosa")
#     elif pl <= 5:
#         return("Virginica")
#     else:
#         return("Versicolor")

def classify_iris(sl, sw, pl, pw):
    if pl < 2:
        return ("setosa")
    elif sl >= 4.9 and pl >= 4.9:
        return ("virginica")
    else:
        return ("versicolor")

good_predictions = 0
len = test_set.shape[0]
for i in range(len):
    # print(test_set[i])
    sl = test_set[i][0]
    sw = test_set[i][1]
    pl = test_set[i][2]
    pw = test_set[i][3]

    if classify_iris(sl, sw, pl, pw).lower() == test_set[i][4]:
        good_predictions = good_predictions + 1
    else:
        print(test_set[i])

print(good_predictions)
print(good_predictions / len * 100, "%") # 42%


# print(train_set)
for iris in train_set:
    if iris[4] == "virginica":
        print(iris)


