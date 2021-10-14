# QUESTION - 1
import pandas as pd
from scipy import stats

df = pd.read_csv("House Price.csv")

x = df['Sq_Feet']
y = df['Price']

slope, intercept, r, p, std_err = stats.linregress(x,y)

def myfunc(x):
    return slope * x + intercept

IP = [2000,3000,1500]

mymodel = list(map(myfunc, x))

for i in IP:
    print(int(myfunc(i)))
    
# QUESTION - 2
import pandas as pd
from sklearn import linear_model

df = pd.read_csv("Stock Index.csv")

X = df[['Interest','Unemp_R']]
Y = df['Stock_IP']

regr = linear_model.LinearRegression()
regr.fit(X,Y)

prediction = regr.predict([[1.5,5.8]])
print(prediction)