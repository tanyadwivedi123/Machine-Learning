import matplotlib.pyplot as plt
plt.figure(1)
plt.subplot(131)

plt.plot([1,2,3])
plt.subplot(132)
plt.plot([7,8,9])
plt.figure(2)
plt.plot([11,12,13])
plt.figure(1)
plt.subplot(131)
plt.title('Easy as 1,2,3')
plt.show()