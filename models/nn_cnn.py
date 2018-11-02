from keras.layers import Conv1D, MaxPooling1D, Dense, Dropout, Flatten
from keras.layers.advanced_activations import LeakyReLU
from keras.models import Model


def create_cnn(model_input, num_classes):
    """
    define cnn model

    :param model_input:
    :param num_classes:
    :return:
    """
    x = Conv1D(56, kernel_size=3, activation='relu', padding="same",
               kernel_initializer='he_normal')(model_input)
    x = Conv1D(filters=64, kernel_size=1, padding="same", activation='relu')(x)
    x = MaxPooling1D(pool_size=2)(x)
    x = Dropout(0.5)(x)
    x = Conv1D(filters=128, kernel_size=3, padding="same", activation='relu')(x)
    x = Conv1D(filters=256, kernel_size=3, padding="valid", activation='relu')(x)
    x = MaxPooling1D(pool_size=2)(x)
    x = Dropout(0.5)(x)
    x = Flatten()(x)
    x = Dense(256)(x)
    x = LeakyReLU()(x)
    x = Dropout(0.5)(x)
    x = Dense(256)(x)
    x = LeakyReLU()(x)
    x = Dense(num_classes, activation='softmax')(x)
    model = Model(model_input, x, name='cnn')
    print(model.summary())
    return model
