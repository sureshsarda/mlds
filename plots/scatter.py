import matplotlib.pyplot as plt
import random

xy = [(i, random.randint(20, 40)) for i in range(10)]
x = [it[0] for it in xy]
y = [it[1] for it in xy]

plt.scatter(x, y, color='black')

plt.plot(x, y, color='blue')
# plt.plot(diabetes_X_test, diabetes_y_pred, color='blue', linewidth=3)

plt.xticks(())
plt.yticks(())

plt.show()
