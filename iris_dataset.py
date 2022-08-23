#!/usr/bin/env python
# coding: utf-8

# # IRIS DATASET

# In[7]:


import numpy as np

import pandas as pd
data = pd.read_csv(r"C:\Users\priyadharshini\iris.csv")
from sklearn.model_selection import train_test_split
#/----------------Function for perceptron algorithm --------------/
def perceptron(c,X,d,w,iter):
    for n in range(1,iter):# Number of iterations  = 20
        print("Iteration :",n)
        for i, x in enumerate(X):
            net = np.dot(X[i],w)
            if net > 0:
                out = 1
            else:
                out = -1
            r = c*(d[i] - out)
            delta_w = r*x
            w = delta_w+w
            print (n, i, w)
    return w
#/---------------------Function for testing the perceptron-----------/

def test_perceptron(final_out,X,w):
    for i,x in enumerate(X):
        net = np.dot(X[i],w)
        if net>0:
            out = 1
        else:
            out = -1
        final_out = final_out+[out]
    return final_out

#---------------Training---------------------------------/
X = data.iloc[:,0:4].values
print ("Inputs", X)
d1=data.iloc[:,4].values
d=np.where(d1=='Iris-setosa',1,-1)
print ("Teacher values", d)
#Splitting the data set
X_train, X_test, y_train, y_test = train_test_split(X, d, test_size=0.33)#computing training and testing sets of x and y
print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)
w= ([0,0,0,0])
print ("initial values of weights", w)
c = 1
iterations = 20
print ("Training")
print ("----------")
final_weight = perceptron(c,X_train,y_train,w,iterations)#calculating final_weight
print ("Final sets of weights: ", final_weight)
#-----------------Testing-------------------------------/
final_out = []
print ("Testing")
print ("--------")
final_output = test_perceptron(final_out,X_test,final_weight)#calculating final_output
print ("Final output: ", final_output)
print ("Original Teacher values",y_test)


# In[ ]:




