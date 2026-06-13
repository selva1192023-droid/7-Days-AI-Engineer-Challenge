import tensorflow as tf
from tensorflow import keras
import numpy as np

x = np.array([1, 2, 3, 4, 5], dtype=float)
y = np.array([2, 4, 6, 8, 10], dtype=float)

model = keras.Sequential([
    keras.layers.Dense(units=1, input_shape=[1])
])

model.compile(optimizer='sgd', loss='mean_squared_error')

model.fit(x, y, epochs=100, verbose=0)

prediction = model.predict([6])

print("Prediction for 6:")
print(prediction)
