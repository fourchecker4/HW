import numpy as np
import matplotlib.pyplot as plt

array1 = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9, 10, 11, 12]])
print(array1)

xpoints1 = np.arange(1, 7)
ypoints1 = np.arange(5, 11)

print(xpoints1)
print(xpoints1)

plt.plot(xpoints1, ypoints1)
plt.show()

x = np.array([0, 1, 2, 3, 4])
y1 = np.array([0, 1, 2, 3, 4])
y2 = np.array([5, 6, 7, 8, 9])
y3 = np.array([9, 10, 11, 12, 13])

plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)
plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.show()

i1 = np.array([1, 3, 5, 1])
j1 = np.array([1, 5, 1, 1])

plt.subplot(1, 2, 1)
plt.plot(i1, j1, '*:r')
plt.title('Triangle')

i2 = np.array([1, 1, 5, 5, 1])
j2 = np.array([1, 5, 5, 1, 1])

plt.subplot(1, 2, 2)
plt.plot(i2, j2, '*:g')
plt.title('Square')

plt.show()



