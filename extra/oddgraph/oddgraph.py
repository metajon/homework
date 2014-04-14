import matplotlib.pyplot as plt

y = [1,2,3]
x = [3,3,3]

plt.plot(x, y, 'ro')

plt.xlabel('Day')
plt.ylabel('Time')
plt.title('Times of visits')

plt.show()