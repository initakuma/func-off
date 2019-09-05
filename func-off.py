import tensorflow as tf
import numpy as np
from tensorflow import keras

model = tf.keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])
model.compile(optimizer='sgd', loss='mean_squared_error')

n=int(input("Enter the number of x-y pairs: "))
x=np.zeros(n)
y=np.zeros(n)

for i in range(n):
    tmp1=float(input("Enter x: "))
    tmp2=float(input("Enter y: "))
    x[i-1]=tmp1
    y[i-1]=tmp2


model.fit(x, y, epochs=1337)

q = float(input("Enter x for which y is to be predicted: "))
print("predicted y is:- ")
print(model.predict([q]))
