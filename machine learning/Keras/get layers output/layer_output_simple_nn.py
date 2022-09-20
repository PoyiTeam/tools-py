"""
keras model layers output example
"""

#%% build and train model
from tensorflow.keras.layers import Dense, InputLayer
from tensorflow.keras import Sequential, optimizers, Model
from tensorflow.keras import metrics
import numpy as np
import matplotlib.pyplot as plt


def BuildModel(input_shape):

    model = Sequential(name="simple_cnn1d")
    model.add(
        InputLayer(input_shape=input_shape, batch_size=None, name="input"))
    model.add(Dense(7, activation="sigmoid", name="dense_1"))
    model.add(Dense(9, activation="sigmoid", name="dense_2"))
    model.add(Dense(1, activation="sigmoid", name="output"))
    adam = optimizers.Adam(learning_rate=0.0001)
    model.compile(optimizer=adam,
                  loss="mse",
                  metrics=[metrics.MeanSquaredError(name="mse")])
    model.build()
    model.summary()
    return model


x = np.array([[0.02, 0.04, 0.06, 0.08, 0.10], [0.2, 0.4, 0.6, 0.8, 1]])

input_shape = x[0].shape
y = np.array([[0.01], [0.1]])
model = BuildModel(input_shape)
model.fit(x=x, y=y, epochs=20)

#%%
layer_num = len(model.layers)
for i in range(layer_num):
    print("index: {}, layer name: {}".format(i, model.layers[i].name))

#%%-----modify target_layer_num to specific layer-----
target_layer_num = layer_num

#%%
layers_output = []
layers_name = []
for i in range(target_layer_num):
    print("index:{}, layer name:{}".format(i, model.layers[i].name))
    layers_name.append(model.layers[i].name)
    layers_output.append(model.layers[i].output)

model_intermediate = Model(inputs=model.inputs,
                           outputs=layers_output,
                           name="intermediate_model")
model_intermediate.summary()
layers_activation = model_intermediate.predict(x)  # layers outputs

layers_output = {}
for i in range(layer_num):
    layers_output[layers_name[i]] = layers_activation[i]

# %%
i = 0
for layer_activation in layers_activation:
    fig = plt.figure(i + 1, figsize=(8, 5))
    fig.suptitle(layers_name[i])
    j = 0
    for activation in layer_activation:
        ax = fig.add_subplot(1, 2, j + 1)
        ax.set_title("data num: {}".format(j))
        ax.plot(range(len(activation)), activation, marker="x", linestyle="")
        j += 1
    i += 1
# %%
