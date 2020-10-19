import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import export_graphviz
import pydot
from sklearn import metrics
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
train_features = pd.read_excel("./final_TRAIN.xlsx", header=None)
test_features = pd.read_excel("./final_TEST.xlsx", header=None)

train_labels = np.array(train_features[208])
test_labels = np.array(test_features[208])
# print(labels)
train_features= train_features.drop(208, axis = 1)
test_features= test_features.drop(208, axis = 1)
# print(features.head(5))
feature_list = list(train_features.columns)
# print(feature_list)
train_features = np.array(train_features)
test_features = np.array(test_features)


print('Training Features Shape:', train_features.shape)
print('Training Labels Shape:', train_labels.shape)
print('Testing Features Shape:', test_features.shape)
print('Testing Labels Shape:', test_labels.shape)




X_train = train_features
X_test = test_features

regressor = RandomForestRegressor(n_estimators=20, random_state=0)
regressor.fit(X_train, train_labels)
y_pred = regressor.predict(X_test)

clf = RandomForestClassifier(max_depth=8, random_state=0)
clf.fit(X_train, train_labels)
pred = clf.predict(X_test)
# print(confusion_matrix(test_labels,y_pred.round()))
print(classification_report(test_labels,y_pred.round()))
# print(accuracy_score(test_labels, y_pred.round()))

print("confusion_matrix----")
print(confusion_matrix(test_labels,y_pred.round()))

print('Accuracy: ',accuracy_score(test_labels, pred.round()))

print('TEST LABELS: ',test_labels)

print("Prediction ", pred)


print(set(train_labels) - set(y_pred))

new_df = pd.DataFrame(columns=['TEST_LABELS', 'Prediction'])
for i in range(len(test_labels)):
    new_df = new_df.append({'TEST_LABELS':test_labels[i], 'Prediction': pred[i]}, ignore_index=True)
new_df.to_excel("C:/Users/sumed/Desktop/Spring20/Feb27/March22/output/Prediction_accuracyOf9.xlsx")


# print(metrics.f1_score(test_labels, y_pred.round(), average='weighted', labels=np.unique(y_pred.round())))
