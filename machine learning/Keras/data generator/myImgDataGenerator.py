import numpy as np
from PIL import Image
from tensorflow.keras.utils import Sequence, to_categorical
from sklearn.preprocessing import LabelEncoder
import math


class DataGen(Sequence):
    def __init__(self, dataset, batch_size, input_size, shuffle=True):
        self.dataset = dataset
        self.shuffle = shuffle
        if self.shuffle:
            self.ShuffleDataset()

        self.labelEncoder = LabelEncoder()
        self.x = self.dataset["x"]
        self.y = self.labelEncoder.fit_transform(self.dataset["y"])
        print("y shape:", np.shape(self.y))
        self.y = to_categorical(self.y)
        self.input_size = input_size
        self.batch_size = batch_size

    def __len__(self):
        return math.ceil(len(self.x) / self.batch_size)

    def __getitem__(self, idx):
        batch_x = self.x[idx * self.batch_size:(idx + 1) * self.batch_size]
        batch_y = self.y[idx * self.batch_size:(idx + 1) * self.batch_size]
        batch_x = self.GetData(batch_x)

        return batch_x, batch_y

    def get_data(self, batch_x):
        """
        function: load data
        You can change the method for different data type
        """

        batch_data_shape = [len(batch_x)]
        batch_data_shape.extend(self.input_size)
        batch_data = np.zeros(batch_data_shape)
        i = 0
        for path in batch_x:
            img = Image.open(path)
            img = np.asarray(img)[:, :, 1].reshape(self.input_size) / 255
            batch_data[i] = img
            i += 1

        return batch_data

    def shuffle_dataset(self):
        self.dataset = self.dataset.sample(frac=1).reset_index(drop=True)

    def on_epoch_end(self):
        if self.shuffle:
            self.ShuffleDataset()
            self.x = self.dataset["x"]
            self.y = self.labelEncoder.fit_transform(self.dataset["y"])
            self.y = to_categorical(self.y)
