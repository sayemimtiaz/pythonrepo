from keras.models import Model
from keras.layers import Concatenate, Dense, LSTM, Input, concatenate
from keras.optimizers import Adagrad
import tensorflow as tf

model.add(tf.keras.layers.Flatten(input_shape = (my, input, shape)))

first_dense = Dense(1, )(first_input)

second_input = Input(shape=(2, ))
second_dense = Dense(1, )(second_input)

merge_one = concatenate([first_dense, second_dense])

third_input = Input(shape=(1, ))
merge_two = concatenate([merge_one, third_input])

ada_grad = Adagrad(lr=0.1, epsilon=1e-08, decay=0.0)
model.compile(optimizer=ada_grad, loss='binary_crossentropy',
               metrics=['accuracy'])
