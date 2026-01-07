import sys

import pygame



def wyswietl_menu(obraz, wymiary_okna):
    global kolor_3x3, kolor_4x4, kolor_5x5
    dzialanie = True
    rozmiar = 3
    camera = True
    czcionka = pygame.font.SysFont('Arial', 20, bold=True)
    czcionka_tytul = pygame.font.SysFont('Arial', 60, bold=True)
    czcionka_autor = pygame.font.SysFont('Arial', 20, bold=True, italic=True)


    tytul = czcionka_tytul.render("Witaj w 2048", True, (255, 255, 0))
    autor = czcionka_autor.render("Autor: Albert Bajera", True, (255, 255, 0))
    tekst_3x3 = czcionka.render("3x3", True, (255, 255, 0))
    tekst_4x4 = czcionka.render("4x4", True, (255, 255, 0))
    tekst_5x5 = czcionka.render("5x5", True, (255, 255, 0))

    srodek_tytul = wymiary_okna[0] // 2 - tytul.get_width() // 2

    srodek = wymiary_okna[0] //2

    tekst2 = czcionka.render("Zagraj", True, (0, 255, 0))
    srodek_graj = wymiary_okna[0] // 2 -200
    przycisk_graj = pygame.Rect(srodek_graj, 400, 400, 100)
    pygame.draw.rect(obraz, (0, 0, 255), przycisk_graj,border_radius=10)
    miejsce = tekst2.get_rect(center=przycisk_graj.center)


    wybierz = czcionka.render("Wybierz rozmiar mapy:", True, (255, 255, 0))
    przycisk_3x3 = pygame.Rect(srodek-140, 300, 80, 50)
    przycisk_4x4 = pygame.Rect(srodek-40, 300, 80, 50)
    przycisk_5x5 = pygame.Rect(srodek+60, 300, 80, 50)

    srodek_wybierz = wymiary_okna[0] // 2 - wybierz.get_width() // 2

    przycisk_camera = pygame.Rect(wymiary_okna[0]/2-150, 550, 300, 50)




    # przycisk_ustawienia = pygame.Rect(200, 400, 400, 100)
    # pygame.draw.rect(obraz, (255, 255, 255), przycisk_ustawienia)
    #
    # tekst2 = czcionka.render("Zagraj", True, (0, 255, 0))
    # tekst3 = tekst2.get_rect(center=przycisk_ustawienia.center)
    # obraz.blit(tekst2, tekst3)


    while dzialanie:
        obraz.fill((200, 200, 200))


        if camera:
            camera_kolor = (0,100,0)
            tekst_camera = czcionka.render("Gesty", True, (255, 255, 0))
        else:
            camera_kolor = (0,0,100)
            tekst_camera = czcionka.render("Klawiatura", True, (255, 255, 0))

        pygame.draw.rect(obraz, camera_kolor, przycisk_camera,border_radius=10)
        obraz.blit(tekst_camera, tekst_camera.get_rect(center=przycisk_camera.center))

        obraz.blit(tytul, (srodek_tytul, 60))
        obraz.blit(autor, (50, 650))
        pygame.draw.rect(obraz, (200, 60, 100), przycisk_graj, border_radius=10)
        obraz.blit(tekst2, miejsce)
        obraz.blit(wybierz, (srodek_wybierz,200))

        if rozmiar == 3:
            kolor_3x3 = (0, 30, 200)
            kolor_4x4 = (0, 0, 100)
            kolor_5x5 = (0, 0, 100)
        elif rozmiar == 4:
            kolor_3x3 = (0, 0, 100)
            kolor_4x4 = (0, 30, 200)
            kolor_5x5 = (0, 0, 100)
        elif rozmiar == 5:
            kolor_3x3 = (0, 0, 100)
            kolor_4x4 = (0, 0, 100)
            kolor_5x5 = (0, 30, 200)

        pygame.draw.rect(obraz, kolor_3x3, przycisk_3x3, border_radius=10)
        pygame.draw.rect(obraz, kolor_4x4, przycisk_4x4, border_radius=10)
        pygame.draw.rect(obraz, kolor_5x5, przycisk_5x5, border_radius=10)

        obraz.blit(tekst_3x3, tekst_3x3.get_rect(center=przycisk_3x3.center))
        obraz.blit(tekst_4x4, tekst_4x4.get_rect(center=przycisk_4x4.center))
        obraz.blit(tekst_5x5, tekst_5x5.get_rect(center=przycisk_5x5.center))






        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if przycisk_graj.collidepoint(event.pos):

                    return rozmiar, camera
                if przycisk_3x3.collidepoint(event.pos):
                    rozmiar = 3
                if przycisk_4x4.collidepoint(event.pos):
                    rozmiar = 4
                if przycisk_5x5.collidepoint(event.pos):
                    rozmiar = 5
                if przycisk_camera.collidepoint(event.pos):
                    camera = not camera

            if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                pygame.quit()
                sys.exit()
    return None
