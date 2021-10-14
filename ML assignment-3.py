import pandas as pd

df1=pd.read_csv('AWCustomers.csv')

df2=pd.read_csv('AWSales.csv')

df1.head()

df3=df1.drop(['Title','FirstName','MiddleName','LastName','Suffix','AddressLine1','AddressLine2','City','StateProvinceName','LastUpdated','PhoneNumber'],axis=1)

df3.head()
df3.describe()
print(df3.shape)
print(df3.dtypes)

#Handling Null Values
df3.isna().sum()

#AWSales data
df2.head()
print(df2.shape)

#Normalisation using MinMaxScaler
from sklearn.preprocessing import MinMaxScaler
scaling1=MinMaxScaler()
scaling1.fit_transform(df3[['YearlyIncome']])

#Standardisation(Z-score Nomalisation)(mean=0,sd=1)
from sklearn.preprocessing import StandardScaler
scaling2=StandardScaler()
df3['YearlyIncome']=scaling2.fit_transform(df3[['YearlyIncome']])

df3.Occupation.unique()

print(len(df3['CountryRegionName'].unique()),len(df3['Education'].unique()),len(df3['Occupation'].unique()))

CountryRegionName_dummies=pd.get_dummies(df3.CountryRegionName)
Education_dummies=pd.get_dummies(df3.Education)
Occupation_dummies=pd.get_dummies(df3.Occupation)
# print(CountryRegionName_dummies)
print(Occupation_dummies)
# print(Education_dummies)

df4=pd.concat([df3,CountryRegionName_dummies,Education_dummies,Occupation_dummies],axis='columns')
print(df4)

df5=df4.drop(['CountryRegionName','Education','Occupation'],axis='columns')
print(df5)

print(df3)

#another way for one hot encoding is
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()

df3.CountryRegionName=le.fit_transform(df3.CountryRegionName)
df3.Occupation=le.fit_transform(df3.Occupation)
df3.Education=le.fit_transform(df3.Education)

print(df3)

from sklearn.preprocessing import OneHotEncoder
lbh=OneHotEncoder(handle_unknown='ignore')

cnt = pd.DataFrame(lbh.fit_transform(df3[['CountryRegionName']]).toarray(),dtype=int)
edu = pd.DataFrame(lbh.fit_transform(df3[['Education']]).toarray(),dtype=int)
occ = pd.DataFrame(lbh.fit_transform(df3[['Occupation']]).toarray(),dtype=int)

df6=pd.concat([df3,cnt,edu,occ],axis='columns')
print(df6)

df7=df6.drop(['CountryRegionName','Education','Occupation'],axis='columns')
print(df7)