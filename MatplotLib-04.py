import matplotlib.pyplot as plt
plt.plot([1,2,3,4,5],[1,2,3,4,5], 'g1',label='line 1',linewidth=2)
plt.plot([1,2,3,4,5],[1,4,9,16,25],'r|',label='line 2')
plt.axis([0,6,0,25])
plt.legend()
plt.show()
