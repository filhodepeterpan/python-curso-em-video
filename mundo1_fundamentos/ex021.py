# Tocando um MP3
# Versão com pygame-ce

from pygame import mixer, time

mixer.init()
mixer.music.load("assets/bella_ciao.mp3")
mixer.music.play()

print("Tocando Bella Ciao...")

while mixer.music.get_busy():
    time.Clock().tick(10)

print("Obrigado por ouvir! Cheque os direitos autorais no diretório assets/copyrights.txt")