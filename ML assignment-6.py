import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

df=pd.read_csv('Irisnew.csv')
print(df)

X=df.iloc[:,:-1]
print(X)

Y=df.iloc[:,-1]
print(Y)

scaler=StandardScaler()
X_std=scaler.fit_transform(X)

clf=LogisticRegression(random_state=0,multi_class='ovr')

model=clf.fit(X_std,Y)

new_obervation=[[.5,.5,.5,.5]]

print(model.predict(new_obervation))

print(model.predict_proba(new_obervation))