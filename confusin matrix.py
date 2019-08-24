from pandas import read_csv
from sklearn.model_selection import KFold
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
filename='indians-diabetes.data.csv'
names=['preg','plas','pres','skin','test','mass','pedi','age','class']
dataframe=read_csv(filename,names=names)
array=dataframe.values
x=array[:,0:8]
y=array[:,8]
test_size=0.33
seed=7
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=test_size,random_state=seed)
model.fit(x_train,y_train)
predicted=model.predict(x_test)
matrix=confusion_matrix(y_test,predicted)
print(matrix)
