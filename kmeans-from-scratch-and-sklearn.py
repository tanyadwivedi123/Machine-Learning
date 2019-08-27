 xxxfrom copy import deepcopy
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import warnings
warnings.filterwarnings(action = "ignore")
#plt.style.use('ggplot')

# Importing the dataset
data = pd.read_csv('KMeansData.csv')
print("Input Data and Shape")
print(data.shape)
print data.head()

# Getting the values and plotting it
f1 = data['V1'].values
f2 = data['V2'].values

plt.scatter(f1, f2, c='black', s=7)
plt.show()




X = np.array(list(zip(f1, f2)))


# Euclidean Distance Caculator
def dist(a, b, ax=1):
    return np.linalg.norm(a - b, axis=ax)

# Number of clusters
k = 3
# X coordinates of random centroids
C_x = np.random.randint(0, np.max(X)-20, size=k)
print "C_x = " , C_x
# Y coordinates of random centroids
C_y = np.random.randint(0, np.max(X)-20, size=k)
print "C_y = " , C_y

C = np.array(list(zip(C_x, C_y)), dtype=np.float32)
print("Initial Centroids")
print(C)

# Plotting along with the Centroids
plt.scatter(f1, f2,  s=7)
plt.scatter(C_x, C_y, marker='*', s=200, c='r')
plt.show()

# To store the value of centroids when it updates
C_old = np.zeros(C.shape)   #C.shape = [3,2]
print "C =  \n", C
print "C_old \n" , C_old

print 'len(X) = ' , len(X)

# Cluster Lables(0, 1, 2)
clusters = np.zeros(len(X))
print "clusters : = " , clusters    #zero filled numpy array of 3000 elements


print "np.linalg.norm(C - C_old, axis=1)" , np.linalg.norm(C - C_old, axis=1)

# Error func. - Distance between new centroids and old centroids
error = dist(C, C_old, None)
# Loop will run till the error becomes zero
while error != 0:
    # Assigning each value to its closest cluster
    for i in range(len(X)):
        distances = dist(X[i], C)      # distances = [ 12 , 50 , 9 ]
        cluster = np.argmin(distances) # cluster = 2
        clusters[i] = cluster
    # Storing the old centroid values
    C_old = deepcopy(C)
    # Finding the new centroids by taking the average value
    for i in range(k):  # k=3  because we have to find 3 centroid locaton
        points = [  X[j] for j in range(len(X)) if clusters[j] == i  ]
        C[i] = np.mean(points, axis=0)
    error = dist(C, C_old, None)

colors = ['b', 'c', 'r', 'g', 'y', 'm']
fig, ax = plt.subplots()
for i in range(k):    # k=3
        points = np.array([X[j] for j in range(len(X)) if clusters[j] == i])
        ax.scatter(points[:, 0], points[:, 1], s=200, c=colors[i])

ax.scatter(C[:, 0], C[:, 1], marker='*', s=250, c='y')

plt.show()

print "Final Centroid : " , C









'''
==========================================================
scikit-learn
==========================================================
'''

from sklearn.cluster import KMeans
print "KMeans of sklearn"
# Number of clusters
kmeans = KMeans(n_clusters=3)

# Importing the dataset
data = pd.read_csv('KMeansData.csv')

f1 = data['V1'].values
f2 = data['V2'].values
X = np.array(list(zip(f1, f2)))

# Fitting the input data
kmeans = kmeans.fit(X)

# Getting the cluster labels
labels = kmeans.predict(X)
print "labels : " , labels
# Centroid values
centroids = kmeans.cluster_centers_

# Comparing with scikit-learn centroids
print("sklearn:Centroid values")
print("KMeans:Manual centroid")
print(C)
print("KMeans sklearn:centroids")
print(centroids) # From sci-kit learn