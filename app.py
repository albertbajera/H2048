import subprocess
import sys
import time

game = subprocess.Popen([sys.executable, "main.py"])
print("Uruchomiono gre")
time.sleep(2)

camera = subprocess.Popen([sys.executable, "cam_player.py"])
print("Uruchomiono kamere")
try:
    while True:
        if game.poll() != None: #sprawdzanie czy ktorys z procesow zostal zamkniety zwraca None gdy proces pracuje
            print("Koniec gry")
            break
        if camera.poll() != None:
            print("Koniec kamery")
            break
finally:
    game.terminate()
    camera.terminate()



