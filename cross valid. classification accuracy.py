from pandas import read_csv
from sklearn.model_selection import KFold
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
filename='indians-diabetes.data.csv'
names=['preg','plas','pres','skin','test','mass','pedi','age','class']
dataframe=read_csv(filename,names=names)
array=dataframe.values
x=array[:,0:8]
y=array[:,8]
kfold=KFold(n_splits=10,random_state=7)
model=LogisticRegression()
scoring='accuracy'
results=cross_val_score(model,x,y,cv=kfold,scoring=scoring)
print ("Accuracy: %.3f(%.3f)") % (results.mean()*100, results.std()*100)