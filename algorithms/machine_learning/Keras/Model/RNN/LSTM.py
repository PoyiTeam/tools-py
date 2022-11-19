#%% ver.latest
from tensorflow.keras.layers import LSTM, Dense, Dropout, BatchNormalization
from tensorflow.keras import Sequential, optimizers, regularizers
from tensorflow.keras.constraints import max_norm


#%% build model
def BuildLSTM(model_name, time_step, features_num):
    model = Sequential(name=model_name)
    model.add(
        LSTM(256,
             input_shape=(time_step, features_num),
             activation="tanh",
             recurrent_activation="sigmoid",
             return_sequences=True,
             return_state=False,
             kernel_regularizer=regularizers.l2(l2=0.0001),
             recurrent_regularizer=regularizers.l2(l2=0.0001),
             bias_regularizer=regularizers.l2(l2=0.0001),
             kernel_constraint=max_norm(2),
             recurrent_dropout=0.1,
             name="LSTM_1"))

    model.add(
        LSTM(128,
             input_shape=(time_step, features_num),
             activation="tanh",
             recurrent_activation="sigmoid",
             return_sequences=True,
             return_state=False,
             kernel_regularizer=regularizers.l2(l2=0.0001),
             recurrent_regularizer=regularizers.l2(l2=0.0001),
             bias_regularizer=regularizers.l2(l2=0.0001),
             kernel_constraint=max_norm(2),
             recurrent_dropout=0.1,
             name="LSTM_2"))

    model.add(Dropout(0.2))

    model.add(
        Dense(64,
              activation="relu",
              kernel_regularizer=regularizers.l2(l2=0.0001),
              bias_regularizer=regularizers.l2(l2=0.0001),
              kernel_constraint=max_norm(3),
              name="Dense_1"))

    model.add(
        Dense(1,
              activation="relu",
              kernel_regularizer=regularizers.l2(l2=0.0001),
              bias_regularizer=regularizers.l2(l2=0.0001),
              kernel_constraint=max_norm(3),
              name="Dense_2"))

    opt = optimizers.Adam(learning_rate=0.001)
    model.compile(optimizer=opt, loss="mae", metrics=["mae"])
    model.summary()

    return model