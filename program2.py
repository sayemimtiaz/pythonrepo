import keras
from keras.layers import Dense,Sequential,TimeDistributed

model = Sequential()

def fun():
  model.add(keras.models.Ballow())

if a==2:
  model.add(keras.models.Shallow(a=2))
elif a==3:
   fun()
   model.add(keras.models.Tallow(a=2))
elif a>5:
  model.add(keras.models.Kallow(a=2))
else:
  model.add(keras.models.Nallow(a=2))
  
num_features=100
model.add(LSTM(100, input_dim=num_features))
model.add(TimeDistributed(keras.Dense(1, activation='sigmoid')))
