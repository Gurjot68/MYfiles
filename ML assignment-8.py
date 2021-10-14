from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV

dataset=datasets.load_breast_cancer()
print(dataset.data)
print()

X_train,X_test,Y_train,Y_test=train_test_split(dataset.data,dataset.target,test_size=0.2,random_state=0)

knn=KNeighborsClassifier()

knn.fit(X_train,Y_train)

predict=knn.predict_proba(X_test)[:9]
print(predict)
print()

grid_params = {'n_neighbors': [1,3,5,7,9,11,13,15]}

gs = GridSearchCV(KNeighborsClassifier(),grid_params,verbose=1,cv=3,n_jobs=-1)
results = gs.fit(X_train, Y_train)
print(results.best_params_)
print()

score = knn.score(X_test,Y_test)
print(score)