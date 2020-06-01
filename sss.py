# noinspection PyUnresolvedReferences
import numpy as np
# noinspection PyUnresolvedReferences
import pandas as pd
# noinspection PyUnresolvedReferences
import matplotlib.pyplot as plt

data=pd.read_csv('/Users/xiaofeifei/PycharmProjects/untitled0/data/train.data')
# print data
X = data.iloc[:80,:2].values
Y = data.iloc[:80,2].values
# print X
# print Y

plt.scatter(X[:40, 0], X[:40, 1], color='blue', marker='o', label='Positive')
plt.scatter(X[40:, 0], X[40:, 1], color='red', marker='x', label='Negative')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.legend(loc = 'upper left')
plt.title('Original Data')
plt.show()























