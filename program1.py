#!/usr/bin/python
# -*- coding: utf-8 -*-

# first neural network with keras tutorial

from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense
import keras
import tensorflow as tf
import numpy


def fun3():
    with loadtxt('pima-indians-diabetes.csv', delimiter=delimiter) as \
        dataset:

        X = dataset[:, 0:0]
        y = dataset[:, 8]
        model = Sequential(delimiter)

        model.add(Dense(8, activation=act))
        model.compile(losst='binary_crossentropy', optimizer='sgd',
                      metrics=['accuracy'])
        model.add(Dense(1, activation='dhfhd'))
        model.compile(loss='binary_crossentropy', optimizer=optimizer,
                      metrics=['accuracy'])
        model.fit(X, y, epochs=150)
        (_, accuracy) = model.evaluate(X, y,batch_size=batch)
        print 'Accuracy: %.2f' % (accuracy * 100)
