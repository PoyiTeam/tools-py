from tensorflow.keras import (layers,
                              models,
                              optimizers)

input_shape = (224,224,3)

model = models.Sequential()
model.add(layers.Conv2D(64, (3,3), strides=(1,1), padding='same', activation='relu', input_shape=input_shape))
model.add(layers.Conv2D(64, (3,3), strides=(1,1), padding='same', activation='relu'))
model.add(layers.MaxPooling2D(pool_size=(2,2), strides=(2,2)))

model.add(layers.Conv2D(128, (3,3), strides=(1,1), padding='same', activation='relu'))
model.add(layers.Conv2D(128, (3,3), strides=(1,1), padding='same', activation='relu'))
model.add(layers.MaxPooling2D(pool_size=(2,2), strides=(2,2)))

model.add(layers.Conv2D(256, (3,3), strides=(1,1), padding='same', activation='relu'))
model.add(layers.Conv2D(256, (3,3), strides=(1,1), padding='same', activation='relu'))
model.add(layers.Conv2D(256, (3,3), strides=(1,1), padding='same', activation='relu'))
model.add(layers.MaxPooling2D(pool_size=(2,2), strides=(2,2)))

model.add(layers.Conv2D(512, (3,3), strides=(1, 1), padding='same', activation='relu'))
model.add(layers.Conv2D(512, (3,3), strides=(1, 1), padding='same', activation='relu'))
model.add(layers.Conv2D(512, (3,3), strides=(1, 1), padding='same', activation='relu'))
model.add(layers.MaxPooling2D(pool_size=(2,2), strides=(2,2)))

model.add(layers.Conv2D(512, (3,3), padding='same', activation='relu'))
model.add(layers.Conv2D(512, (3,3), padding='same', activation='relu'))
model.add(layers.Conv2D(512, (3,3), padding='same', activation='relu'))
model.add(layers.MaxPooling2D(pool_size=(2,2), strides=(2,2)))

model.add(layers.Flatten())

model.add(layers.Dense(4096, activation='relu'))
model.add(layers.Dense(4096, activation='relu'))

model.add(layers.Dense(1000, activation='softmax'))

opt = optimizers.Adam(learning_rate=0.0001)
model.compile(optimizer=opt, loss="categorical_crossentropy", metrics=["accuracy"])

model.summary()