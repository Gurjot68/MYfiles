import numpy as np
from sklearn.datasets import load_iris

iris = load_iris()

X = iris.data
Y = iris.target

from sklearn.model_selection import train_test_split

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.30,random_state=12)

from sklearn.naive_bayes import GaussianNB

model = GaussianNB()

model = model.fit(X_train,Y_train)

Y_pred = model.predict(X_test)
Y_pred2 = model.predict(X_train)

from sklearn.metrics import confusion_matrix

Conf_Mat = confusion_matrix(Y_test,Y_pred)
print("Confusion Matrix => ")
print(Conf_Mat)

print()

TP = 0
TN = 0
FP = 0
FN = 0

Y_test = np.array(Y_test).reshape(-1,1)

for i in range(len(Y_pred)):
    if(Y_test[i]==1 and Y_pred[i]==1):
        TP = TP + 1
    if(Y_test[i]==1 and Y_pred[i]==0):
        FN = FN + 1
    if(Y_test[i]==0 and Y_pred[i]==1):
        FP = FP + 1
    if(Y_test[i]==0 and Y_pred[i]==0):
        TN = TN + 1
print("True Positive => ",TP)
print("True Negative => ",TN)
print("False Positive => ",FP)
print("False Negative => ",FN)

from sklearn.metrics import accuracy_score,f1_score,recall_score,precision_score

print()

Accuracy = accuracy_score(Y_test,Y_pred)
print("Accuracy = ",Accuracy)

Recall = recall_score(Y_test,Y_pred,average = 'macro')
print("Recall = ",Recall)

F1 = f1_score(Y_test,Y_pred,average = 'macro')
print("F-1 Score = ",F1)

Precision = precision_score(Y_test,Y_pred,average = 'macro')
print("Precision = ",Precision)

Accuracy2 = accuracy_score(Y_train,Y_pred2)
print("Accuracy-2 = ",Accuracy2)

Recall2 = recall_score(Y_train,Y_pred2,average = 'macro')
print("Recall-2 = ",Recall2)

F1_2 = f1_score(Y_train,Y_pred2,average = 'macro')
print("F1-Score-2 = ",F1_2)

Precision2 = precision_score(Y_train,Y_pred2,average = 'macro')
print("Precision-2 = ",Precision2)