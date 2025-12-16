import cv2
import mediapipe

cam = cv2.VideoCapture(0)
szerokosc = cam.get(cv2.CAP_PROP_FRAME_WIDTH)
wysokosc = cam.get(cv2.CAP_PROP_FRAME_HEIGHT)

siatka = mediapipe.solutions.face_mesh
sledzenie = siatka.FaceMesh(max_num_faces=1,min_detection_confidence=0.5, min_tracking_confidence=0.5)



while True:
    poprawne,klatka = cam.read()
    klatka = cv2.flip(klatka,1)
    klatka2 = cv2.cvtColor(klatka, cv2.COLOR_BGR2RGB)

    if not poprawne:
        print('Blad kamery')
        break

    punkty = sledzenie.process(klatka2)

    if punkty.multi_face_landmarks:
        twarz = punkty.multi_face_landmarks[0]
        nos = twarz.landmark[1] #1 to pkt na nosie
        nos_x = int(nos.x*szerokosc)
        nos_y = int(nos.y*wysokosc)
        cv2.circle(klatka, (nos_x,nos_y), 5, (255, 0, 0), 2)



    cv2.imshow('Kamera', klatka)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()


