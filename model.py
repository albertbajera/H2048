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
    tf.keras.layers.Dense(64, input_shape=(40,), activation='relu'), #relu pomaga sieci uczyc sie skomplikowanych wzorcow
    tf.keras.layers.Dropout(0.2), #losowe wylaczdnie 20 pr neuronow aby nie uczyl sie na pamiec
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(4, activation='softmax') #softmax zwraca ze model jest pewny na tyle procent

])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy']) #categorical_crossentropy jak bardzo model sie myli
model.fit(wartosc_train,kierunek_train,epochs=100,batch_size=8,validation_data=(wartosc_test,kierunek_test)) #epochs przejscie danych 100 razy,batch_size po 8 danych jest aktualizacja
model.save('model.h5')