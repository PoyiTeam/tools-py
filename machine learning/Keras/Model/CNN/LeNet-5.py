from tensorflow.keras import (Sequential,
                              optimizers)
from tensorflow.keras.layers import (Conv2D,
                                     AveragePooling2D,
                                     Flatten,
                                     Dense)

input_shape = (32, 32, 1)

model = Sequential()

model.add(Conv2D(20, kernel_size=(5, 5), strides=(1, 1), activation='tanh', input_shape=input_shape, padding='valid'))
model.add(AveragePooling2D(pool_size=(2, 2), strides=(2, 2), padding='valid'))

model.add(Conv2D(50, kernel_size=(5, 5), strides=(1, 1), activation='tanh', padding='valid'))
model.add(AveragePooling2D(pool_size=(2, 2), strides=(2, 2), padding='valid'))

model.add(Flatten())
model.add(Dense(120, activation='tanh'))
model.add(Dense(84, activation='tanh'))

model.add(Dense(10, activation='softmax'))

opt = optimizers.Adam(learning_rate=0.0001)
model.compile(loss='categorical_crossentropy', optimizer='sgd', metrics=['accuracy']) 

model.summary()