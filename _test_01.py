# noinspection PyUnresolvedReferences
import numpy as np
# noinspection PyUnresolvedReferences
import pandas as pd
# noinspection PyUnresolvedReferences
import matplotlib.pyplot as plt

data=pd.read_csv('/Users/xiaofeifei/PycharmProjects/untitled0/data/train.data')
data_test=pd.read_csv('/Users/xiaofeifei/PycharmProjects/untitled0/data/test.data')
# print data
# read the data
X = data.iloc[40:121,[0,3]].values
T = data_test.iloc[:20,[0,3]].values
#change to real number

# print X
w = np.zeros((1,2))
# first w1 and w2 value
# print w
l=1
b = 0
# first value of b
w1 = w[0][0]
w2 = w[0][1]
#get w from array
A = 0
while(l<=20):#20 iteration
    l=l+1
    for i in range(0,40):
        y = 1
        a = w1*X[i,0]+w2*X[i,1]
        # print y*a
        if (y*a <= 0):

            w1 = w1+y*X[i,0]
            w2 = w2+y*X[i,1]
            b = b + y
        else:
            w1 = w1
            w2 = w2
            b=b
        # print w1,w2,b






    for j in range(41,80):
        y = -1
        a = w1* X[j,0]+w2*X[j,1]
        if (y * a <= 0):
            w1 = w1 + y * X[j, 0]
            w2 = w2 + y * X[j, 1]
            b = b + y
        else:
            w1 = w1
            w2 = w2
            b=b
        # print w1,w2,b
    x1=0
    y1=-b/w2
    x2=10
    y2=(-w1/w2)*10-(b/w2)
    #image
    plt.scatter(X[:40, 0], X[:40, 1], color='blue', marker='o', label='Positive')
    plt.scatter(X[40:, 0], X[40:, 1], color='red', marker='x', label='Negative')
    plt.plot([x1, x2], [y1, y2], 'black')
    # plt.xlim(4,7.5)
    # plt.ylim(1.5,4.5)
    plt.title('Each interation pic')
    plt.show()

    if(l<=10):
        A = A + (w1*T[l,0]+w2*T[l,1])
        if(A>=0):
            signA = 0
        else:
            signA = 1

    print w1, w2, b









