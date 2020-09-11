import keras

num_features=10
model = Sequential()
model.add(LSTM(100, input_dim=num_features, return_sequences=True))
model.add(TimeDistributed(Dense(1, activation='sigmoid')))
