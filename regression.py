import numpy as np


class RegressionModel:
    def __init__(self, x_train, y_train):

        assert(len(x_train) == len(y_train))

        x = x_train
        x_squared = np.square(x)
        x_sum = np.sum(x)
        x_squared_sum = np.sum(x_squared)

        y = y_train
        y_sum = np.sum(y)

        xy = x * y
        xy_sum = np.sum(xy)

        self.slope = (len(x) * xy_sum - x_sum * y_sum) / \
            (len(x) * x_squared_sum - x_sum ** 2)

        self.intercept = (y_sum - self.slope * x_sum) / len(x)


class RegressionModelSelfMade:
    def __init__(self, x_train, y_train):

        assert(len(x_train) == len(y_train))

        x = x_train
        x_squared = [i ** 2 for i in x]
        x_sum = sum(x)
        x_squared_sum = sum(x_squared)

        y = y_train
        y_sum = sum(y)

        xy = [1] * len(x_train)

        for i in range(len(x)):
            xy[i] = x[i] * y[i]

        xy_sum = sum(xy)

        self.slope = (len(x) * xy_sum - x_sum * y_sum) / \
            (len(x) * x_squared_sum - x_sum ** 2)

        self.intercept = (y_sum - self.slope * x_sum) / len(x)


a = [1, 2, 3, 4]
b = [2, 4, 6, 8]

model = RegressionModelSelfMade(a, b)

print(model.slope)

print(model.intercept)
