import matplotlib.pyplot as plt
from keras.callbacks import EarlyStopping


def model_train(model, X_train, y_train, X_val, y_val, batch_size, num_epochs):
    history = model.fit(x=X_train, y=y_train, batch_size=batch_size, epochs=num_epochs, verbose=0,
                        validation_data=(X_val, y_val))
    return history


def model_train_early_stop(model, X_train, y_train, X_val, y_val, batch_size, num_epochs):
    history = model.fit(x=X_train, y=y_train, batch_size=batch_size, epochs=num_epochs, verbose=0,
                        validation_data=(X_val, y_val),
                        callbacks=[EarlyStopping(monitor='val_acc', patience=10, verbose=0,
                                                 mode='auto')])
    return history


def evaluate_accuracy(model, X_test, y_test):
    score = model.evaluate(X_test, y_test, verbose=0)
    return score[1]


def visualize_history(history, prefix='', plot_loss=False):
    accuracy = history.history['acc']
    val_accuracy = history.history['val_acc']
    loss = history.history['loss']
    val_loss = history.history['val_loss']
    epochs = range(len(accuracy))
    plt.plot(epochs, accuracy, 'bo', label='Training accuracy')
    plt.plot(epochs, val_accuracy, 'b', label='Validation accuracy')
    plt.title(prefix + 'Training and validation accuracy')
    plt.legend()
    if plot_loss:
        plt.figure()
        plt.plot(epochs, loss, 'bo', label='Training loss')
        plt.plot(epochs, val_loss, 'b', label='Validation loss')
        plt.title(prefix + 'Training and validation loss')
        plt.legend()
    plt.show()
