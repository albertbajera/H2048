import cv2
import mediapipe
import pyautogui
import  tensorflow as tf
import numpy as np


cam = cv2.VideoCapture(0)
szerokosc = cam.get(cv2.CAP_PROP_FRAME_WIDTH)
wysokosc = cam.get(cv2.CAP_PROP_FRAME_HEIGHT)

nr_klatki = 0
wartosci = []
dlugosc = 20
coldown = 0


model = tf.keras.models.load_model('model.h5')
klasy = ['dol','gora','lewo','prawo']

siatka = mediapipe.solutions.face_mesh
sledzenie = siatka.FaceMesh(max_num_faces=1,min_detection_confidence=0.5, min_tracking_confidence=0.5)

ostatni_ruch_tekst = " "
wyswietlanie_licznik = 0


while True:

    poprawne,klatka = cam.read()
    if not poprawne:
        print('Blad kamery')
        break


    klatka = cv2.flip(klatka,1)


    klatka2 = cv2.cvtColor(klatka, cv2.COLOR_BGR2RGB)
    nr_klatki += 1
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(klatka, str(nr_klatki), (10, 30), font, 1, (255, 0, 255), 2, cv2.LINE_AA)


    punkty = sledzenie.process(klatka2)
    if punkty.multi_face_landmarks:
        twarz = punkty.multi_face_landmarks[0]
        nos = twarz.landmark[1] #1 to pkt na nosie


        wartosci.append([nos.x,nos.y])


        if len(wartosci)>dlugosc:
            wartosci.pop(0)

        if len(wartosci) == dlugosc and coldown == 0:

            delty = [0.0,0.0]
            for i in range (1,len(wartosci)):
                dx = wartosci[i][0] - wartosci[i-1][0]
                dy = wartosci[i][1] - wartosci[i-1][1]
                delty.extend([dx,dy])


            wejscie = np.array([delty])
            predykcja = model.predict(wejscie,verbose=0)
            idx = np.argmax(predykcja)
            pewnosc = predykcja[0][idx]

            if pewnosc >0.8:
                kierunek = klasy[idx]
                ostatni_ruch_tekst = kierunek
                wyswietlanie_licznik = 20
                print(f"KIERUNEK: {kierunek}, PEWNOSC: {pewnosc}")
                match kierunek:
                    case "dol":
                        pyautogui.press('down')
                    case "gora":
                        pyautogui.press('up')
                    case "lewo":
                        pyautogui.press('left')
                    case "prawo":
                        pyautogui.press('right')

                coldown = 20
                wartosci = []

        if coldown > 0:
            coldown -= 1

        cv2.circle(klatka, (int(nos.x*szerokosc),int(nos.y*wysokosc)), 5, (255, 0, 0), 2)
        if wyswietlanie_licznik > 0:
            cv2.putText(klatka, f"Wykonano ruch:{ostatni_ruch_tekst}", (10, 700), font, 2, (0, 0, 255), 2, cv2.LINE_AA)
            wyswietlanie_licznik -= 1
        klatka_mala = cv2.resize(klatka,(480,320))
        cv2.imshow('Player',klatka_mala)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break




cam.release()
cv2.destroyAllWindows()
