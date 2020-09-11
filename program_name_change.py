import keras

num_features=100
model = Sequential()
model.add(LSTM(100, input_dim=num_features))
model.add(TimeDistributed(Dense(1, activation='sigmoid')))
