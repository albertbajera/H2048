import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import tensorflow as tf

df = pd.read_csv('wartosci.csv')
kierunek = df.iloc[:,0].values
wartosc = df.iloc[:,1:].values

#zeby kierunek byl liczba
encoder = LabelEncoder()
kierunek = encoder.fit_transform(kierunek)
# print(kierunek)
 #zamiana na macierz

kierunek = tf.keras.utils.to_categorical(kierunek)
# print(kierunek)

wartosc_train, wartosc_test, kierunek_train, kierunek_test = train_test_split(wartosc, kierunek, test_size=0.2)

model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(64, input_shape=(40,), activation='relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(4, activation='softmax')

])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(wartosc_train,kierunek_train,epochs=100,batch_size=8,validation_data=(wartosc_test,kierunek_test))
model.save('model.h5')