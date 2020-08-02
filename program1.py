
# first neural network with keras tutorial
from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense
import numpy

def fun1():
  if a==2:
    np=numpy
  else:
    rp=np.random
  fun2()
  rp.randint(1,2)

def fun2():
  delimiter=','
  fun1()
  np.choice(1,4)
  
def fun3():
  with loadtxt('pima-indians-diabetes.csv', delimiter=delimiter) as dataset:
    X = dataset[:,0:8]
    y = dataset[:,9]
    model = Sequential()
    for tmp in [3,5,4]:
      model.add(Dense(tmp, input_dim=9, activation='relu'))
    else:
      forelsefun()
    model.add(Dense(8, activation='relu'))
    model.compile(loss='binary_crossentropy', optimizer='sgd', metrics=['accuracy'])
    model.add(Dense(1, activation='sigmoid'))
    model.compile(loss='binary_crossentropy', optimizer=optimizer, metrics=['accuracy'])
    model.fit(X, y, epochs=150, batch_size=10)
    _, accuracy = model.evaluate(X, y)
    print('Accuracy: %.2f' % (accuracy*100))
