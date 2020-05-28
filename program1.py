import numpy as np
import keras

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

try:
    class MyClass:
        "This is my second class"
        a = 10

        def func(self):
            print('Hello')

        class Inner:
            """Inner Class"""

            def inner_display(self, msg):
                print(msg)
except NameError:
    print("Found error")

a = b[:-1]
a = b[:]
temp[temp != 1] = 0
a = b[1:2]
a = b[[2, 3]]

print("hello world", 1, 2)
img_dim = a[2]
new_dim = a.shape[1]

# One hot encoding array

helloFunc((a, 2), b)

possible_actions = np.arange(0, num_env_actions)
actions_1_hot = np.zeros((num_env_actions, num_env_actions))

# Create testing enviroment
env = gym.make('Pong-v0')
env.reset()

# initialize training matrix with random states and actions
dataX = np.random.random((5, num_env_variables + num_env_actions))
# Only one output for the total score / reward
dataY = np.random.random((5, 1))

# initialize training matrix with random states and actions
apdataX = np.random.random((5, num_env_variables))
apdataY = np.random.random((5, num_env_actions))


def custom_error(y_true, y_pred, Qsa):
    cce = 0.001 * (y_true - y_pred) * Qsa
    return cce


# nitialize the Reward predictor model
model = Sequential()

model.add(Dense(2048, activation='relu', input_dim=(10, 2)))

model.add(Dense(2048, activation='relu', input_dim=dataX.shape[1]))
model.add(Dropout(0.25))
model.add(Dense(128, activation='relu' + 'gelo'))
model.add(Dropout(0.5))
model.add(Dense(dataY.shape[1]))
opt = optimizers.adam(lr=learning_rate)
model.compile(loss='mse', optimizer=opt, metrics=['accuracy'])

num = [2, 3]

for i in num:
    print(i)

i = 1
while i < 6:
    print(i)
    i += 1
