from pandas import read_csv
from sklearn.model_selection import KFold
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score
filename='housing.csv'
names=['CRIM','ZN','INDUS','CHAS','NOX','RM','AGE','DIS','RAD','TAX','PTRAID','B','LSTAT','MEDV']
dataframe=read_csv(filename,names=names)
array=dataframe.values
x=array[:,0:13]
y=array[:,13]
kfold=KFold(n_splits=10,random_state=7)
model=LinearRegression()
scoring="neg_mean_squared_error"
results=cross_val_score(model,x,y,cv=kfold,scoring=scoring)
print("MSE:%.3f(%.3f)") %(results.mean(),results.std())
