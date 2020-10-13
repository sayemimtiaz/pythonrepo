from keras.models import Model
from keras.layers import Dense,Flatten
from keras.applications import vgg16
from keras import backend as K

model = vgg16.VGG16(weights='imagenet', include_top=True)

model.input

model.summary(line_length=150)

model.layers.pop()
model.layers.pop()

model.summary(line_length=150)

new_layer = Dense(10, activation='softmax', name='my_dense')

inp = model.input
out = new_layer(model.layers[-1].output)

model2 = Model(inp, out)
model2.summary(line_length=150)
