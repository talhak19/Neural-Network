from keras.models import Sequential
from keras.layers import Dropout, Dense
from sklearn.model_selection import train_test_split
import numpy as np

def split_data(df):

    X_train, X_test, y_train, y_test = train_test_split(df[['budget', 'popularity',"vote_average","revenue","vote_count","rating"]], df['user_types'], test_size=0.2, random_state=42)

    X_train = np.asarray(X_train).astype(np.float32)
    y_train = np.asarray(y_train).astype(np.float32)
    X_test = np.asarray(X_test).astype(np.float32)
    y_test = np.asarray(y_test).astype(np.float32)

    return X_train,X_test, y_train, y_test

def create_nn_model_and_fit(df):
    X_train,X_test, y_train, y_test = split_data(df)

    # Modeli oluşturalım
    model = Sequential()
    model.add(Dense(128, input_dim=X_train.shape[1], activation='relu'))
    model.add(Dense(64,activation='relu'))
    model.add(Dense(32,activation='relu'))
    model.add(Dense(16,activation='relu'))

    model.add(Dense(1, activation='sigmoid'))

    # Modeli derleyelim
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

    # Modeli Eğitelim
    model.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_test, y_test))


    scores = model.evaluate(X_test, y_test)
    print("Test accuracy:", scores[1])