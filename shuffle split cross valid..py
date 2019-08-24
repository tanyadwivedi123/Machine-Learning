from pandas import read_csv
from sklearn.model_selection import ShuffleSplit
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
filename='indians-diabetes.data.csv'
names=['preg','plas','pres','skin','test','mass','pedi','age','class']
dataframe=read_csv(filename,names=names)
array=dataframe.values
x=array[:,0:8]
y=array[:,8]
test_size=0.33
seed=7
shufflesplit=ShuffleSplit(n_split,test_size=test_size,random_state=seed)
model=LogisticRegression()
results=cross_val_score(model,x,y,cv=shufflesplit)
print results
print "Accuracy:%.3f" % (results.mean()*100.0)
print "Std.deviation= %.3f" % (results.std() *100.0)
