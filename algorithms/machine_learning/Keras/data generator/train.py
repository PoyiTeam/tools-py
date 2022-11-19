# %%
import myPath
import os
import numpy as np
from model import BuildModel
import pandas as pd
from myDataGenerator import DataGen
import keras.callbacks as callbacks
import matplotlib.pyplot as plt


# %%
def GetDataSet(path_dataset):
    i = 0
    data_x = []
    data_y = []

    data_labels = os.listdir(path_dataset)
    for data_label in data_labels:
        paths_data = os.listdir(path_dataset + data_label)
        for path in paths_data:
            data_x.append(path_dataset + data_label + "/" + path)
            data_y.append(data_label)
    dataset = pd.DataFrame({"x": data_x, "y": data_y})
    i += 1

    return dataset


path_entrance = myPath.GetEntrancePath()
path_dataset = path_entrance + "dataset/"

# %%
path_train = path_dataset + "train/"
path_test = path_dataset + "test/"
test_set = GetDataSet(path_test)
train_set = GetDataSet(path_train)

# %%
path_file = path_train + "/label_1/N09_M07_F10_K001_1_0.csv"
input_size = np.loadtxt(fname=path_file, delimiter=",")
input_size = (len(input_size), 1)

# %%
batch_size = 100
model = BuildModel(input_size)
num_epochs = 5
train_datagen = DataGen(dataset=train_set,
                        batch_size=batch_size,
                        input_size=input_size,
                        shuffle=True)
test_datagen = DataGen(dataset=test_set,
                       batch_size=batch_size,
                       input_size=input_size,
                       shuffle=False)


# %%
class CustomCallback(callbacks.Callback):
    train_loss = []
    train_acc = []
    val_loss = []
    val_acc = []

    def on_epoch_end(self, epoch, logs=None):

        self.train_loss.append(logs["loss"])
        self.train_acc.append(logs["accuracy"])
        self.val_loss.append(logs["val_loss"])
        self.val_acc.append(logs["val_accuracy"])

        print("epoch: {epoch}".format(epoch=(epoch + 1)))
        print("train loss: {:.4f}, train accuracy: {:.2%}".format(
            self.train_loss[epoch], self.train_acc[epoch]))
        print("validation loss: {:.4f}, validation accuracy: {:.2%}".format(
            self.val_loss[epoch], self.val_acc[epoch]))


# %%
myCallback = CustomCallback()
model.fit(train_datagen,
          validation_data=test_datagen,
          epochs=num_epochs,
          callbacks=[myCallback],
          verbose=0)

# %%
