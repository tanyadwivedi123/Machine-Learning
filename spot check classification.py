from pandas import read_csv
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
filename='indian-diabetes.data.csv'
names=['preg','plas','pres','skin','test','mass','pedi','age','class']
dataframe=read_csv(filename,names=names)
array=dataframe.values
x=array[:,0:8]
y=array[:,8]
kfold=KFold(n_splits=10,random_state=7)

#1)Spot checking for Logistic Regression
from sklearn.linear_model import LogisticRegression
model=LogisticRegression()
results=cross_val_score(model,x,y,cv=kfold)
print "Validation score for LogisticRegression:",results.mean()
#2)spot checking for linear discriminant analysis(LDA)
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
model=LinearDiscriminantAnalysis()
results=cross_val_score(model,x,y,cv=kfold)
print "Validation score for  LDA:",results.mean()

#Spot checking for K-Nearest neighbours(kNN)
from sklearn.neighbors import KNeighborsClassifier
model=KNeighborsClassifier()
results=cross_val_score(model,x,y,cv=kfold)
print "Validation score for  kNN:",results.mean()

#5)Spot checking for Classification and regression Trees(CART or just decision tress)
from sklearn.tree import DecisionTreeClassifier
model=DecisionTreeClassifier
results=cross_val_score(model,x,y,cv=kfold)
print "Validation score for  CART Decision Tree:",results.mean()

#Spot checking for Support Vector Machines(SVM)
from sklearn.svm import SVC
model=SVC()
results=cross_val_score(model,x,y,cv=kfold)
print "Validation score for  SVM:",results.mean()
