import numpy as np

import matplotlib.pyplot as plt


class RegressionModel:
    def __init__(self, x, y):

        assert(len(x) == len(y))

        self.x = x
        x_squared = np.square(x)
        x_sum = np.sum(x)
        x_squared_sum = np.sum(x_squared)

        self.y = y
        y_sum = np.sum(y)

        xy = x * y
        xy_sum = np.sum(xy)

        self.slope = (len(x) * xy_sum - x_sum * y_sum) / \
            (len(x) * x_squared_sum - x_sum ** 2)

        self.intercept = (y_sum - self.slope * x_sum) / len(x)

    def predict(self, x):
        return self.slope * x + self.intercept

    def plot(self):
        print("OK")
        plt.plot(self.x, self.y)
        plt.show()



a = np.array([1, 2, 3, 4])
b = np.array([2, 4, 6, 8])


model = RegressionModel(a,b)

model.plot()

