import random
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

l = [random.uniform(1, 1000) for i in range(25)]
x_values = [i for i in range(len(l))]
print(l, x_values)

# counter[0]=index             counter[1]=number of sorted elements
counter = [0, 0]


def animate(i):
    j = counter[0]
    counter[0] += 1
    if l[j] > l[j + 1]:  # for sorting
        l[j], l[j + 1] = l[j + 1], l[j]
    if counter[0] > (len(l) - 2 - counter[1]):  # for resetting the index and increasing the number of sorted elements
        counter[0] = 0
        counter[1] += 1
    plt.cla()
    plt.bar(x_values, l)


ani = FuncAnimation(plt.gcf(), animate, interval=1)
plt.show()
