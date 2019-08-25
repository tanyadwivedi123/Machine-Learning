import matplotlib.pyplot as plt
x=[2,3,4,5,6,7]
y=[4,9,16,25,36,49]
plt.plot(x,y,color='blue',marker='o',linestyle='dashed',markerfacecolor='red',markersize=15)
plt.title("Number with their squared values")
plt.xlabel("------number------",fontsize=14,color='red')
plt.ylabel("------square------",fontsize=14,color='red')
plt.axis([1,8,1,50])
plt.grid(True)
plt.annotate('Square of 5',xy=(5,25),xytext=(3,40),arrowprops=dict(facecolor='black',shrink=.1), )

plt.show()