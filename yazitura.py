#!/usr/bin/env python
import random
from gtts import gTTS
import os

def yazı_tura_çevir():
    cavab = random.choice(["Yazı", "Tura"])
    return cavab


def cavabi_sesli_soyle(cavab):
    tts = gTTS(f"{cavab}", lang='tr') 
    tts.save("cavab.mp3")
    os.system("mpg123 cavab.mp3")  

if __name__ == "__main__":
    input("Yazı-tura atmak için Enter düğmesini tıklayın...")
    cavab = yazı_tura_çevir()
    cavabi_sesli_soyle(cavab)

