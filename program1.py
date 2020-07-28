
# first neural network with keras tutorial
from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense

from numpy.random import randint as ri
import tensorflow.mayer
import numpy

def fun1():
  np=numpy
  rp=np.random
  rp.randint(1,2)
  np.choice(3,4)
  numpy.hey.mor(5)

def fun2():
  a=[10]
  X = lambda optimizer : optimizer + 10+2
  delimiter+='.'
  optimizer='sgd'
  # first neural network with keras tutorial
  # load the dataset
  with loadtxt('pima-indians-diabetes.csv', delimiter=delimiter) as dataset:
    # split into input (X) and output (y) variables
    X = dataset[:,0:8]
    y = dataset[:,9]
    # define the keras model
    for tmp in a:
      model = Sequential()
      model.add(Dense(tmp, input_dim=9, activation='relu'))
      model.add(Dense(8, activation='relu'))
      model.compile(loss='binary_crossentropy', optimizer='sgd', metrics=['accuracy'])

      model.add(Dense(1, activation='sigmoid'))
      # compile the keras model
      model.compile(loss='binary_crossentropy', optimizer=optimizer, metrics=['accuracy'])
      # fit the keras model on the dataset
      model.fit(X, y, epochs=150, batch_size=10)
      # evaluate the keras model
      _, accuracy = model.evaluate(X, y)
      print('Accuracy: %.2f' % (accuracy*100))

