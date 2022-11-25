#Tehtävä 3: Saat annettuna tehtava1.py nimisen tiedoston, jossa on toteutettuna eräs luokka. Tee seuraavat tehtävät:

# 1. Selitä mitä tapahtuu riveillä, joissa on kommentti #mitä tässä tapahtuu? Eli tutustu numpy modulin arange, zeros,
#    cos, sin metodeihin numpyn dokumentaation avulla.

# 2. Lisää luokkaan toiminto, jolla voit tulostaa kosinisignaalin lisäksi sini signaalin. Eli muuta create ja plot metodeja 
#    siten, että create muodostaa myös sini signaalin ja plot metodi tulostaa matplotlib.pyplot subplot funktion avulla kaksi 
#    kuvaa. Toiseen kosinin ja toiseen sinin.

# 3. Toteuta vielä toinen python scripti, jonka nimeksi signalGenerator.py, joka käyttää tehtava1.py skriptiä modulina, josta 
#    se importtaa signalAnalyser luokan. Tee signalGenerator.py tiedostosta sellainen, että käytäjä voi antaa signaalin taajuuden 
#    ja aika-akselin pituuden ja sen jälkeen piirretään vaaditun mittainen ja vaaditun taajuinen sini- ja kosini signaali tehtava1.py 
#    modulin signalAnalyser luokkaa hyödyntäen. Oleta, että näytetaajuus Fs = 1000 Hz ja muista, että tällöin käyttäjä voi antaa 
#    taajuusarvon vain väliltä 0 – 500 Hz. Katso seuraavalta kalvolta miltä ohjelman suorituksen pitäisi näyttää…

from cProfile import label
from signal import signal
import numpy as np
import matplotlib.pyplot as plt

class signalAnalyser:
    def __init__(self,Fs,t):
        print('Constructor of signalAnalyser')
        self.Fs = Fs
        self.Ts = 1/Fs
        self.t = t
        self.xakseli = np.arange(0,t,self.Ts)
        print(self.xakseli)                         # Mitä tässä tapahtuu? 
                                                    # Printaa arangen mukaisen numerosarjan jossa eka parametri määrittelee alkuarvon,
                                                    # toinen loppuarvon ja kolmas askelvälin
                                                    
        self.pituus = int(self.xakseli.size)        # Mitä tässä tapahtuu?
                                                    # Tässä muutetaan kokonaisluvuksi xakseli-muuttujan listalla olevien arvojen määrä 
                                                    # ja asetetaan se omaan muuttujaan
        self.yakseli = np.zeros((1,self.pituus))    # Mitä tässä tapahtuu?
                                                    # Tekee uuden arrayn jossa on yksi rivi ja arvojen määrä muuttujasta ja täytää sen nollilla

    def create(self,f):
        pii = np.pi
        t = self.xakseli
        self.yakseliC = np.cos( 2 * pii * f * t)     # Mitä tässä tapahtuu?
                                                    # Kerrotaan erinäisiä muuttujia cosinin radiaanilla ja asetetaan arvot listaan
        self.yakseliS = np.sin( 2 * pii * f * t)
                                                    
    def plot(self,start,stop):
        plt.figure(1,figsize=(12, 10))
        plt.subplot(211)
        plt.title("Kosini signaali")
        plt.plot(self.xakseli[start:stop],self.yakseliC[start:stop],'-*')
        plt.subplot(212)
        plt.title("Sini signaali")
        plt.plot(self.xakseli[start:stop],self.yakseliS[start:stop],'-*')
        plt.show()

if __name__ == '__main__':
    objC = signalAnalyser(100,2)  # luodaan objekti, jonka konstruktorille Fs = 100 Hz ja t = 2s
    objC.create(2)                # käytetään objektin create funktiota, missä f = 2 Hz
    objC.plot(0,50)               # käytetään objektin plot funktiota, plotataan väli 0 - 50 näytettä.