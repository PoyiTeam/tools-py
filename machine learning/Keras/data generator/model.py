#%%
#from tensorflow.keras.backend import sparse_categorical_crossentropy, softmax
from tensorflow.keras.layers import Conv1D, Dense, InputLayer, Flatten
from tensorflow.keras import Sequential, optimizers
from tensorflow.keras import metrics


def BuildModel(input_shape):

    model = Sequential(name="simple_cnn1d")
    model.add(
        Conv1D(filters=1,
               kernel_size=16001,
               padding="valid",
               input_shape=input_shape,
               activation="relu"))
    model.add(Flatten())
    model.add(Dense(10, activation="relu"))
    model.add(Dense(2, activation="softmax"))
    adam = optimizers.Adam(learning_rate=0.0001)
    model.compile(optimizer=adam,
                  loss="categorical_crossentropy",
                  metrics=[metrics.CategoricalAccuracy(name="accuracy")])
    model.build()
    model.summary()
    return model


# %%
