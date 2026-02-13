H2048 - Projekt popularnej gry 2048 sterowanej przy pomocy ruchów głowy, które są analizowane przez AI

Etapy działania: 
1.  Wykrywanie twarzy - Biblioteka FaceMesh z biblioteki MediaPipe śledzi położenie nosa użytkownika w czasie rzeczywistym.
2.  Przetwarzanie Danych - Program zbiera sekwencję 20 ostatnich klatek, oblicza różnice (delty) ruchu w osi X i Y, tworząc wektor ruchu.
3.  Klasyfikacja AI - prosta sieć neuronowa analizuje wektor i klasyfikuje go jako jeden z 4 kierunków: `Góra`, `Dół`, `Lewo`, `Prawo`.
4.  Symulacja wcisnięcia klawisza - Jeśli pewność sieci przekracza 80%, biblioteka PyAutoGUI symuluje wciśnięcie odpowiedniej strzałki na klawiaturze.

Krótka Wideo Prezentacja 

Rozgrywka:
https://github.com/user-attachments/assets/9f292ff8-862b-4128-990f-654fa26f924a

Trening sieci neuronowej - zmiana wspólrzędnych połozenia nosa przez ostatnie 20 klatek zostanie zapisana do liku CSV:
https://github.com/user-attachments/assets/1f7ca82d-b851-4c11-b12b-1dee54e693e1



Technologie i biblioteki użyte w projekcie: 
- Python
- OpenCV
- MediaPipe
- TensorFlow
- Keras
- NumPy
- PyAutoGUI
