import math
import random

import pygame

pygame.init()
wymiary_okna = (720, 720)
obraz = pygame.display.set_mode(wymiary_okna)
pygame.display.set_caption("H2048")

# pole = [[2, 0, 0], [0, 2, 0], [4, 0, 0]]
pole = [[0,0,0],[0,0,0],[0,0,0]]
wymiay_pola_x = 3
wymiay_pola_y = 3


def rysuj():
    obraz.fill((255, 255, 255))
    for i in range(wymiay_pola_x):
        for j in range(wymiay_pola_y):
            x = 80 + i * 200
            y = 80 + j * 200
            komorka = pole[i][j]

            if komorka == 0:
                k = (230, 255, 230)
            else:
                a = math.log(komorka, 2)
                r = 255 - 17*a
                g = 255
                if r == 0:
                    g = int(g/2)
                b = 255 - 17 * a
                k = (r,g,b)

            pygame.draw.rect(obraz, k, pygame.Rect(x, y, 160, 160))
            tekst = pygame.font.SysFont('Arial', 80).render(str(komorka), True, (0, 0, 0))
            tekst2 = tekst.get_rect(center=(x + 160 / 2, y + 160 / 2))
            obraz.blit(tekst, tekst2)


def wstaw():
    global pole
    puste = []

    for i in range(wymiay_pola_x):
        for j in range(wymiay_pola_y):
            if pole[i][j] == 0:
                puste.append((i, j))

    if puste:
            wiersz, kolumna = random.choice(puste)
            pole[wiersz][kolumna] = 2 #dodaj inne liczby
            return True
    else:
        print("Przegrana")
        return False
# I TO NR.KOLUMNY J TO NR.WIERSZA
def ruch_lewo():
    global pole

    zmiana = True
    while zmiana:  # powtarzaj aż nic się nie zmienia
        zmiana = False
        for i in range(1, wymiay_pola_x):
            for j in range(wymiay_pola_y):

                print(f"I: {i}, J: {j}, POLE:{pole[i][j]}")
                if pole[i][j] == pole[i - 1][j] and pole[i][j] != 0:
                    wartosc = pole[i][j]
                    pole[i][j] = 0
                    pole[i - 1][j] = 2 * wartosc
                    zmiana = True
                elif pole[i][j] != 0 and pole[i - 1][j] == 0:
                    wartosc = pole[i][j]
                    pole[i][j] = 0
                    pole[i - 1][j] = wartosc
                    zmiana = True



# I TO NR.KOLUMNY J TO NR.WIERSZA
def ruch_prawo():
    global pole
    zmiana = True
    while zmiana:
        zmiana = False
        for i in range(wymiay_pola_x-2,-1,-1): #od konca do lewo
            for j in range(wymiay_pola_y):

                print(f"I: {i}, J: {j}, POLE:{pole[i][j]}")
                if pole[i+1][j] == pole[i][j] and pole[i][j] != 0:
                    wartosc = pole[i][j]
                    pole[i+1][j] = 2*wartosc
                    pole[i][j] = 0
                    zmiana = True
                elif pole[i][j] != 0 and pole[i+1][j] == 0:
                    wartosc = pole[i][j]
                    pole[i][j] = 0
                    pole[i+1][j] = wartosc
                    zmiana = True




# I TO NR.KOLUMNY J TO NR.WIERSZA
def ruch_gora():
    global pole
    zmiana = True
    while zmiana:
        zmiana = False
        for i in range(wymiay_pola_x):
            for j in range(1,wymiay_pola_y):  #od poczatku do dolu

                print(f"I: {i}, J: {j}, POLE:{pole[i][j]}")
                if pole[i][j-1] == pole[i][j] and pole[i][j] != 0:
                    wartosc = pole[i][j]
                    pole[i][j-1] = 2*wartosc
                    pole[i][j] = 0
                    zmiana = True
                elif pole[i][j] != 0 and pole[i][j-1] == 0:
                    wartosc = pole[i][j]
                    pole[i][j] = 0
                    pole[i][j-1] = wartosc
                    zmiana = True


# I TO NR.KOLUMNY J TO NR.WIERSZA
def ruch_dol():
    global pole
    zmiana = True
    while zmiana:
        zmiana = False
        for i in range(wymiay_pola_x):
            for j in range(wymiay_pola_y-2,-1,-1): #od dolu do gory

                print(f"I: {i}, J: {j}, POLE:{pole[i][j]}")
                if pole[i][j+1] == pole[i][j] and pole[i][j] != 0:
                    wartosc = pole[i][j]
                    pole[i][j+1] = 2*wartosc
                    pole[i][j] = 0
                    zmiana = True
                elif pole[i][j] != 0 and pole[i][j+1] == 0:
                    wartosc = pole[i][j]
                    pole[i][j] = 0
                    pole[i][j+1] = wartosc
                    zmiana = True

def wynik():
   koniec = True
   while koniec:
       obraz.fill((100,100,100))

       fontObj = pygame.font.SysFont("Arial", 40)
       tekst1 = fontObj.render("Przegrana", True, (255,0,0))
       tekst11 = tekst1.get_rect(center = (360,250))
       obraz.blit(tekst1, tekst11)

       przycisk = pygame.Rect(200,400,400,100)
       pygame.draw.rect(obraz,(255,255,255),przycisk)

       tekst2 = fontObj.render("Zagraj jeszcze raz", True, (0,255,0))
       tekst3 = tekst2.get_rect(center=przycisk.center)
       obraz.blit(tekst2,tekst3)

       pygame.display.flip()

       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               pygame.quit()
           if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
               pygame.quit()
           if event.type == pygame.MOUSEBUTTONDOWN:
               if przycisk.collidepoint(event.pos):
                   reset()
                   koniec = False


def reset():
    global pole
    pole = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    wstaw()

# def zmien_kolor():
#    for i in range(wymiay_pola_x):
#         for j in range(wymiay_pola_y):
#             if pole[i][j] == 0:
#                 tekst = rysuj()
#
#


dziala = True
wstaw()
while dziala:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            wstaw()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            ruch_lewo()

            if not wstaw():
                wynik()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            ruch_prawo()
            if not wstaw():
                wynik()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            ruch_gora()
            if not wstaw():
                wynik()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            ruch_dol()
            if not wstaw():
                wynik()


    rysuj()
    pygame.display.flip()
pygame.quit()
