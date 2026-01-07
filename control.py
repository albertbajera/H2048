import cv2
import mediapipe

import csv

cam = cv2.VideoCapture(0)
szerokosc = cam.get(cv2.CAP_PROP_FRAME_WIDTH)
wysokosc = cam.get(cv2.CAP_PROP_FRAME_HEIGHT)

siatka = mediapipe.solutions.face_mesh
sledzenie = siatka.FaceMesh(max_num_faces=1,min_detection_confidence=0.5, min_tracking_confidence=0.5)

nr_klatki = 0
wartosci = []
dlugosc = 20
kierunek = "Nie ustalono"



while True:

    poprawne,klatka = cam.read()

    klatka = cv2.flip(klatka,1)
    klatka2 = cv2.cvtColor(klatka, cv2.COLOR_BGR2RGB)
    nr_klatki += 1
    #print(nr_klatki)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(klatka, str(nr_klatki), (10, 30),font, 1, (255, 0, 255), 2, cv2.LINE_AA)
    cv2.putText(klatka, str(kierunek), (10, 70), font, 1, (255, 255, 0), 2, cv2.LINE_AA)


    if not poprawne:
        print('Blad kamery')
        break

    punkty = sledzenie.process(klatka2)
    key = cv2.waitKey(1) & 0xFF
    if punkty.multi_face_landmarks:# noqa specjalny komentarz do wylaczenia ostrzezenia bo mediapipe zraca typ ktorego nie rozpozanaje pycharm
        twarz = punkty.multi_face_landmarks[0]# noqa specjalny komentarz do wylaczenia ostrzezenia bo mediapipe zraca typ ktorego nie rozpozanaje pycharm
        nos = twarz.landmark[1] #1 to pkt na nosie


        wartosci.append([nos.x, nos.y])
        if len(wartosci) > dlugosc:
            wartosci.pop(0)

        if key == ord('z'):
            if len(wartosci) == dlugosc:

                delty = [0,0]
                for i in range(1, len(wartosci)):
                    dx = wartosci[i][0] - wartosci[i-1][0]
                    dy = wartosci[i][1] - wartosci[i-1][1]
                    delty.extend([dx, dy])


                with open('wartosci.csv', 'a', newline='') as f:
                    csvwriter = csv.writer(f)
                    wiersz = [kierunek]+delty
                    csvwriter.writerow(wiersz)
                print(f"ZAPISANO: {kierunek}")

        print(nos.x,nos.y)
        cv2.circle(klatka, (int(nos.x*szerokosc),int(nos.y*wysokosc)), 5, (255, 0, 0), 2)


        # cv2.putText(klatka, f"X:{nos_x}",(710,710),font, 1, (0, 255, 0), 2, cv2.LINE_AA)
        # cv2.putText(klatka, f"Y:{nos_y}", (910, 710), font, 1, (0, 255, 0), 2, cv2.LINE_AA)

        # cv2.putText(klatka, f"X :{nos_x} w klatce: {nr_klatki}", (710, 560), font, 1, (0, 255, 0), 2, cv2.LINE_AA)
        # cv2.putText(klatka, f"Y :{nos_y} w klatce: {nr_klatki}", (710, 610), font, 1, (0, 255, 0), 2, cv2.LINE_AA)

    cv2.imshow('Kamera', klatka)
    if key == ord('q'):
        break
    elif key == ord('l'):
        kierunek = "lewo"
    elif key == ord('p'):
        kierunek = "prawo"
    elif key == ord('g'):
        kierunek = "gora"
    elif key == ord('d'):
        kierunek = "dol"


cam.release()
cv2.destroyAllWindows()


