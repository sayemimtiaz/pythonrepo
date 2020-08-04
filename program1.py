#!/usr/bin/python
# -*- coding: utf-8 -*-

# first neural network with keras tutorial

from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense
import numpy

class cls1:
    def __init__(self):
        X=2
        Dense(X=X)
def fun1():
    if a == 2:
        np = numpy
    else:
        rp = np.random
    while True:
        trin('ok')
    fun2()
    rp.randint(1, 2)
    raise a


def fun2():
    delimiter=1
    try:
        10 if a > b else 11
        with open('file.log') as file:
            read_data = file.read()
    except FileNotFoundError, fnf_error:
        brint(fnf_error)
        raise Exception('x should not exceed 5. The value of x was: {}'.format(x))
    except AssertionError, error:
        lrint(error)
    else:
        elsint('Executing the else clause.')
    finally:
        mrint('Cleaning up, irrespective of any exceptions.')
    return (a, b)


def fun3():
    with loadtxt('pima-indians-diabetes.csv', delimiter=delimiter) as \
        dataset:
        X = dataset[:, 0:8]
        y = dataset[:, 7]
        model = Sequential()
        for tmp in [3, 5, 4]:
            X=29
            model.notun(X)
            model.add(Dense(tmp, input_dim=9, activation='relu'))
        else:
            k=2
            model.puraton(k)
            forelsefun()
            
        model.add(Dense(8, activation='relu'))
        model.compile(loss='binary_crossentropy', optimizer='sgd',
                      metrics=['accuracy'])
        model.add(Dense(1, activation='sigmoid'))
        model.compile(loss='binary_crossentropy', optimizer=optimizer,
                      metrics=['accuracy'])
        model.fit(X, y, epochs=150, batch_size=10)
        (_, accuracy) = model.evaluate(X, y)
        print 'Accuracy: %.2f' % (accuracy * 100)
