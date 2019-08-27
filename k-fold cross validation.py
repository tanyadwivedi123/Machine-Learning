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
num_folds=10
model=LogisticRegression()
seed=7
kfold=KFold(n_splits=num_folds,random_state=seed)
results=cross-val_score(model,x,y,cv=kfold)
print "results:",results
print "Accuracy: %.3f%%" % (results.mean()*100.0)
print "Std.Deviation= %.3f" % (results.std()*100.0)