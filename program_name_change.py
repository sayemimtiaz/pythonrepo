import keras

if a==2:
  print(1)
elif a==3:
  print(5)
elif a>5:
  print("hi")
else:
  print("There you go")
num_features=100
model = Sequential()
model.add(LSTM(100, input_dim=num_features))
model.add(TimeDistributed(Dense(1, activation='sigmoid')))
