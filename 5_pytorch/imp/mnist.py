r"""The mnist dataset.

:reference: https://blog.csdn.net/qq_45032341/article/details/105292379
"""
from keras.datasets import mnist
(train_X, train_y), (test_X, test_y) = mnist.load_data()

print(train_X.shape)

