from sklearn.metrics import mean_squared_error
from keras.models import Sequential
from sklearn.preprocessing import StandardScaler
from keras.layers import Dropout, Dense
from sklearn.model_selection import train_test_split
import numpy as np


def split_data(df):

    X_train, X_test, y_train, y_test = train_test_split(df[['budget',"runtime", 'popularity',"vote_average","revenue","user_types"]],df['rating'], test_size=0.2)

    return X_train,X_test, y_train, y_test



def create_nn_model_and_fit(df):

    X_train,X_test, y_train, y_test = split_data(df)

    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)


    # Modeli oluşturalım
    model = Sequential()
    model.add(Dense(16, input_dim=X_train.shape[1], activation='relu'))
    model.add(Dense(8, activation='relu'))
    # Dropout katmanı overfittingden kacmak icin; %20 ağırlık sıfırlanacak)
    model.add(Dropout(0.2))
    model.add(Dense(1, activation='linear'))


    model.compile(optimizer='Adam',loss='mean_squared_error')

    model.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_test, y_test))
    predictions = model.predict(X_test)

    # Tahminlerin doğruluğu için
    mse = mean_squared_error(y_test, predictions)

    # Ölçülen MSE değerini RMSE'ye dönüstürüyoruz
    rmse = np.sqrt(mse)
    print("Tahmin Doğruluğu (RMSE):", rmse)