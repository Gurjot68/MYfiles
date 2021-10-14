import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#%matplotlib inline

from sklearn.datasets import load_digits

digits = load_digits(n_class=10)

digits.keys()

digits.target_names

digits['DESCR']

x=digits.data
print(x)

print(x.shape)

x=pd.DataFrame(x)
print(x)

y=digits.target
y=pd.DataFrame(y)
print(y)

df=pd.DataFrame(x)
df["class"]=y
print(df)

fig, axes=plt.subplots(nrows=1,ncols=4,figsize=(12,3))
for ax, image, label in zip(axes,digits.images,digits.target):
    ax.imshow(image,cmap='binary')
    ax.set_title('Training:%i'%label)
    
from sklearn.preprocessing import StandardScaler

#standardisation of the data
ss = StandardScaler()
x1 = pd.DataFrame(ss.fit_transform(x))
print(x1)

# Computing the covarience matrix
cov_mat = x1.cov()
print(cov_mat)

corr_mat = x1.corr()
print(corr_mat)

#Calculating eigen-values and eigen-vectors
eig_vals, eig_vecs = np.linalg.eig(cov_mat)
print(eig_vals.shape)
print(eig_vecs.shape)

print(eig_vals)

print(eig_vecs[1])

#Store the eigenvalues and eigenvectors in pair and sort acc. to eigen-values
eig_pairs = [(np.abs(eig_vals[i]),eig_vecs[:,i]) for i in range(len(eig_vals))]
srtd_eig_pairs = sorted(eig_pairs,reverse=True,key=lambda x:x[0])
for i in eig_pairs:
    print(i[0])

l = []
for i in range(len(eig_vals)):
    l.append(eig_vals[i]/np.sum(eig_vals))
print(l)

pc1=x1.dot(eig_vecs.T[0])
pc2=pd.DataFrame(x1.dot(eig_vecs.T[1]))
pc3=pd.DataFrame(x1.dot(eig_vecs.T[2]))
pc4=pd.DataFrame(x1.dot(eig_vecs.T[3]))

df2=pd.DataFrame(pc1,columns=["PC1"])
df3=(pd.concat([df2,pc2,pc3,pc4,y],axis="columns"))
df3=pd.DataFrame(df3)
df3.columns=["PC1","PC2","PC3","PC4","Labels"]
print(df3)

xx=df3[["PC1","PC2","PC3","PC4"]]
sns.heatmap(xx.corr(),annot=True)

df3.plot(kind="scatter",x="PC1",y="PC2")