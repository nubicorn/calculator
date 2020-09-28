import numpy as np
from scipy import stats as sts
import matplotlib.pyplot as plt


class Calculator:
    def __init__(self, data):
        data.sort()
        self.data = data
        self.mean = np.mean(data)
        self.med = np.median(data)
        self.mode = sts.mode(data)
        self.min = data[0]
        self.max = data[-1]
        self.range = self.max - self.min
        self.q1 = np.median(data[:len(data) // 2])
        self.q3 = np.median(data[(len(data) / 2).__round__():])
        self.iqr = self.q3 - self.q1
        self.outliers = [x for x in data if x < self.q1 - self.iqr * 1.5 or x > self.q3 + self.iqr * 1.5]
        self.variance = np.var(data)
        self.std = np.std(data)

    def z_score(self, x):
        return (x - self.mean) / self.std

    def percentile(self, x):
        return (self.data.index(x) + 1) / len(self.data) * 100

    def percentage(self, x):
        return np.percentile(self.data, x)

    def summary(self):
        print(f'Minimum: {self.min}')
        print(f'Quartile 1: {self.q1}')
        print(f'Median: {self.med}')
        print(f'Quartile 3: {self.q3}')
        print(f'Maximum: {self.max}')


data_set = [-73, 5, 8, 3, 2, 9, 7, 60, 100]
stats = Calculator(data_set)
stats.summary()
plt.boxplot(stats.data)
plt.show()
