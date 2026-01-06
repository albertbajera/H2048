import math
import random
import subprocess
import sys
import pygame
from menu import wyswietl_menu



def wczytaj_rekord(rozmiar):
    nazwa = f"rekord{rozmiar}x{rozmiar}.txt"
    with open(nazwa,"r") as f:
        return int(f.read())

def zapisz_rekord(rozmiar, nowy_rekord):
    nazwa = f"rekord{rozmiar}x{rozmiar}.txt"
    with open(nazwa,"w") as f:
        f.write(str(nowy_rekord))



pygame.init()
wymiary_okna = (720, 720)
obraz = pygame.display.set_mode(wymiary_okna)
pygame.display.set_caption("H2048")



program = True
while program:
    rozmiar, camera = wyswietl_menu(obraz, wymiary_okna)
    rekord = wczytaj_rekord(rozmiar)

    proces_camera = False
    if camera:
        print("Wlaczanie Kamery")
        proces_camera = subprocess.Popen([sys.executable, "cam_player.py"])

    # pole = [[2, 0, 0], [0, 2, 0], [4, 0, 0]]

    if rozmiar == 3:
        pole = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        wymiay_pola_x = 3
        wymiay_pola_y = 3
        value_size = 160
        odstep = 200
        margin_x = 80
    elif rozmiar == 4:
        pole = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        wymiay_pola_x = 4
        wymiay_pola_y = 4
        value_size = 130
        odstep = 155
        margin_x = 60
    elif rozmiar == 5:
        pole = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
        wymiay_pola_x = 5
        wymiay_pola_y = 5
        value_size = 100
        odstep = 120
        margin_x = 70

    wynikk = 0


    def rysuj():

        global font_size
        obraz.fill((200, 200, 200))

        prostokott = pygame.Rect(200, 40, 400, 40)
        pygame.draw.rect(obraz, (50, 50, 50), prostokott, border_radius=10)

        czcionka = pygame.font.SysFont('Arial', 20, bold=True)
        tekst = czcionka.render(f"Twoj Wynik:{wynikk}    Twoj rekord:{rekord} ", True, (255, 255, 0))
        miejsce = tekst.get_rect(center=prostokott.center)
        obraz.blit(tekst, miejsce)

        for i in range(wymiay_pola_x):
            for j in range(wymiay_pola_y):
                x = margin_x + i * odstep
                y = 120 + j * odstep
                komorka = pole[i][j]

                if komorka == 0:
                    k = (230, 255, 230)
                else:
                    a = math.log(komorka, 2)
                    r = 255 - 17 * a
                    g = 255
                    if r == 0:
                        g = int(g / 2)
                    b = 255 - 17 * a
                    k = (r, g, b)

                pygame.draw.rect(obraz, k, pygame.Rect(x, y, value_size, value_size), border_radius=10)
                if komorka != 0:
                    if rozmiar == 3:
                        font_size = 80
                    elif rozmiar == 4:
                        font_size = 60
                    elif rozmiar == 5:
                        font_size = 40
                    tekst = pygame.font.SysFont('Arial', font_size).render(str(komorka), True, (0, 0, 0))
                    tekst2 = tekst.get_rect(center=(x + value_size / 2, y + value_size / 2))
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
            lista_do_watawienia = [2, 4]
            prawdopodobioenstwo = [.8, .2]
            liczba = random.choices(lista_do_watawienia, weights=prawdopodobioenstwo)
            pole[wiersz][kolumna] = liczba[0]

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
            for i in range(wymiay_pola_x - 2, -1, -1):  # od konca do lewo
                for j in range(wymiay_pola_y):

                    print(f"I: {i}, J: {j}, POLE:{pole[i][j]}")
                    if pole[i + 1][j] == pole[i][j] and pole[i][j] != 0:
                        wartosc = pole[i][j]
                        pole[i + 1][j] = 2 * wartosc
                        pole[i][j] = 0
                        zmiana = True
                    elif pole[i][j] != 0 and pole[i + 1][j] == 0:
                        wartosc = pole[i][j]
                        pole[i][j] = 0
                        pole[i + 1][j] = wartosc
                        zmiana = True


    # I TO NR.KOLUMNY J TO NR.WIERSZA
    def ruch_gora():
        global pole
        zmiana = True
        while zmiana:
            zmiana = False
            for i in range(wymiay_pola_x):
                for j in range(1, wymiay_pola_y):  # od poczatku do dolu

                    print(f"I: {i}, J: {j}, POLE:{pole[i][j]}")
                    if pole[i][j - 1] == pole[i][j] and pole[i][j] != 0:
                        wartosc = pole[i][j]
                        pole[i][j - 1] = 2 * wartosc
                        pole[i][j] = 0
                        zmiana = True
                    elif pole[i][j] != 0 and pole[i][j - 1] == 0:
                        wartosc = pole[i][j]
                        pole[i][j] = 0
                        pole[i][j - 1] = wartosc
                        zmiana = True


    # I TO NR.KOLUMNY J TO NR.WIERSZA
    def ruch_dol():
        global pole
        zmiana = True
        while zmiana:
            zmiana = False
            for i in range(wymiay_pola_x):
                for j in range(wymiay_pola_y - 2, -1, -1):  # od dolu do gory

                    print(f"I: {i}, J: {j}, POLE:{pole[i][j]}")
                    if pole[i][j + 1] == pole[i][j] and pole[i][j] != 0:
                        wartosc = pole[i][j]
                        pole[i][j + 1] = 2 * wartosc
                        pole[i][j] = 0
                        zmiana = True
                    elif pole[i][j] != 0 and pole[i][j + 1] == 0:
                        wartosc = pole[i][j]
                        pole[i][j] = 0
                        pole[i][j + 1] = wartosc
                        zmiana = True


    def wynik():
        koniec = True
        warstwa = pygame.Surface((720, 720))
        warstwa.set_alpha(50)
        warstwa.fill((50, 50, 50))
        while koniec:

            obraz.blit(warstwa, (0, 0))
            fontObj = pygame.font.SysFont("Arial", 20)
            fontObj2 = pygame.font.SysFont("Arial", 40, bold=True, italic=True)
            tekst1 = fontObj2.render("Przegrana", True, (255, 0, 0))
            tekst11 = tekst1.get_rect(center=(360, 250))
            obraz.blit(tekst1, tekst11)

            position = wymiary_okna[0] - 250
            przycisk = pygame.Rect(position, 400, 200, 100)

            pygame.draw.rect(obraz, (255, 255, 255), przycisk, border_radius=10)

            tekst2 = fontObj.render("Zagraj jeszcze raz", True, (0, 255, 0))
            tekst3 = tekst2.get_rect(center=przycisk.center)
            obraz.blit(tekst2, tekst3)

            przycisk_menu = pygame.Rect(50, 400, 200, 100)
            pygame.draw.rect(obraz, (255, 255, 255), przycisk_menu, border_radius=10)

            tekst4 = fontObj.render("Wroc do menu", True, (0, 255, 0))
            tekst5 = tekst4.get_rect(center=przycisk_menu.center)
            obraz.blit(tekst4, tekst5)

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
                    if przycisk_menu.collidepoint(event.pos):
                        return "menu"


    def reset():
        global pole, wynikk
        if rozmiar == 3:
            pole = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        elif rozmiar == 4:
            pole = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        elif rozmiar == 5:
            pole = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

        wynikk = 0
        wstaw()


    dziala = True
    wstaw()
    while dziala:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                if proces_camera:
                    proces_camera.terminate()
                dziala = False
                program = False
                pygame.quit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                wstaw()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                ruch_lewo()
                wynikk += 1
                if wynikk > rekord:
                    rekord = wynikk
                    zapisz_rekord(rozmiar, rekord)
                if not wstaw():
                    result = wynik()
                    if result == "menu":
                        dziala = False
                        if proces_camera:
                            proces_camera.terminate()
                    wynikk = 0

            if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                ruch_prawo()
                wynikk += 1
                if wynikk > rekord:
                    rekord = wynikk
                    zapisz_rekord(rozmiar, rekord)
                if not wstaw():
                    result = wynik()

                    if result == "menu":
                        dziala = False
                        if proces_camera:
                            proces_camera.terminate()
                    wynikk = 0

            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                ruch_gora()
                wynikk += 1
                if wynikk > rekord:
                    rekord = wynikk
                    zapisz_rekord(rozmiar, rekord)
                if not wstaw():
                    result = wynik()
                    if result == "menu":
                        dziala = False
                        if proces_camera:
                            proces_camera.terminate()
                    wynikk = 0

            if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                ruch_dol()
                wynikk += 1
                if wynikk > rekord:
                    rekord = wynikk
                    zapisz_rekord(rozmiar, rekord)
                if not wstaw():
                    result = wynik()
                    if result == "menu":
                        dziala = False
                        if proces_camera:
                            proces_camera.terminate()
                    wynikk = 0

        rysuj()
        pygame.display.flip()
pygame.quit()
