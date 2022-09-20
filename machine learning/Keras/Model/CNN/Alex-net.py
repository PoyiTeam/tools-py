from tensorflow.keras import (layers,
                              models,
                              optimizers)

input_shape = (227,227,3)

model = models.Sequential()
model.add(layers.Conv2D(96, (11,11), strides=(4,4), padding='valid', activation='relu', input_shape=input_shape))  
model.add(layers.MaxPooling2D(pool_size=(3,3), strides=(2,2)))

model.add(layers.Conv2D(256, (5,5), strides=(1,1), padding='same', activation='relu'))  
model.add(layers.MaxPooling2D(pool_size=(3,3), strides=(2,2)))

model.add(layers.Conv2D(384, (3,3), strides=(1,1), padding='same', activation='relu'))  
model.add(layers.Conv2D(384, (3,3), strides=(1,1), padding='same', activation='relu'))  
model.add(layers.Conv2D(256, (3,3), strides=(1,1), padding='same', activation='relu'))
model.add(layers.MaxPooling2D(pool_size=(3,3), strides=(2,2)))
model.add(layers.Flatten())

model.add(layers.Dense(4096, activation='relu'))
model.add(layers.Dropout(0.5))

model.add(layers.Dense(4096, activation='relu'))  
model.add(layers.Dropout(0.5))

model.add(layers.Dense(1000, activation='softmax'))

opt = optimizers.Adam(learning_rate=0.0001)
model.compile(optimizer=opt, loss="categorical_crossentropy", metrics=["accuracy"])

model.summary()