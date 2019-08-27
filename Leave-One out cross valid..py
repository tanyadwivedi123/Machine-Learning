from pandas import read_csv
from sklearn.model_selection import LeaveOneOut
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
filename='indians-diabetes.data.csv'
names=['preg','plas','pres','skin','test','mass','pedi','age','class']
dataframe=read_csv(filename,names=names)
array=dataframe.values
x=array[:,0:8]
y=array[:,8]

loocv=LeaveOneOut()
model=LogisticRegression()
results=cross_val_score(model,x,y,cv=loocv)
print "results:",results
print "result.size:",result.size
print "Sum of positive Results: %i" %(results.sum())
print "Accuracy= %.2f%%" % (results.sum() *100 /results.size)
