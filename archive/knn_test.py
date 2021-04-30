import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
#interactive plotting in separate window

data = pd.read_csv("data/final_video_data_normalized.csv")
correlation_matrix = data.corr()
correlation_matrix['trending']
del data['title']
del data['view_count']
data[["contains_question_mark", "contains_exclamation_mark", "trending", "has_full_cap_word"]] *= 1

#target variable
Y = data['trending']

#features
X = data.iloc[:, :-1]
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.20)

k_range = range(1, 25)
scores = {}
scores_list = []
for k in k_range:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    scores[k] = metrics.accuracy_score(y_test, y_pred)
    scores_list.append(scores[k])
plt.plot(k_range, scores_list)
plt.xlabel('value of K for KNN')
plt.ylabel('Testing Accuracy')
#plt.show()
knn = KNeighborsClassifier(n_neighbors=k)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)
tn, fp, fn, tp = metrics.confusion_matrix(y_test, y_pred).ravel()
print((tn, fp, fn, tp))

