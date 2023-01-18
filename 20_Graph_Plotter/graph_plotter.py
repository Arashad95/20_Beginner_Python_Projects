import matplotlib.pyplot as plt

# x = [2, 4, 5, 4]
# y = [2, 3, 6, 7]

left = [1, 2, 3, 4, 5]
height = [10, 11, 23, 36, 4]

tick_label = ['one', 'two', 'three', 'four', 'five']

plt.bar(left, height, tick_label=tick_label,
        width=0.8, color=['blue', 'orange'])

# plt.plot(x, y, color='green', linestyle='dashed', linewidth=3,
#          marker='o', markerfacecolor='blue', markersize=12)


# plt.ylim(1, 8)
# plt.xlim(1, 8)

plt.xlabel('X Axis')
plt.ylabel('Y Axis')

plt.title("Demo Graph - Bar chart")

plt.show()
