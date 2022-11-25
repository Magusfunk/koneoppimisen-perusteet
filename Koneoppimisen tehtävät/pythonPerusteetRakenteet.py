'''
  Tämän skripti tiedoston tarkoituksena on käydä läpi seuraavia asioita:
  1. aliohjelman rakenne, input parametrien välitys ja tulosten palauts
  2. numpy ja matplotlip.pyplot perusteita, kun niitä tarvitaan myöhemmin
  3. Toistorakenteiden ja kontrollirakenteiden esimerkkejä
  4. Ja kysymyksenä opiskelijoille voisi olla, että miksei input funktiolla voi esimerkissä
     sijoittaa suoraan pysyluupissa funktioon?
'''

import numpy as np
import matplotlib.pyplot as plt

def plot(x,y):
    plt.figure(1)
    plt.plot(x,y,'-r*')
    plt.show()

def makeSignal():
    Fs = 1000.0           # Sampling frequency
    Ts = 1/Fs             # Sampling time interval
    f = 5                 # signal frequency
    #t = np.arange(start=0,stop=1,step=Ts)       # numpy.arange([start, ]stop, [step, ]dtype=None, *, like=None)
    t = np.arange(0,1,Ts)       # numpy.arange([start, ]stop, [step, ]dtype=None, *, like=None)
    sig = np.cos(2*np.pi*f*t)
    return t,sig

def loopfunction():
    pysyluupissa = True
    while(pysyluupissa==True):
        luettu = input("anna True tai False ")
        print(luettu)
        if(luettu=="True"):
            pysyluupissa = True
        else:
            pysyluupissa = False
        print("pysyluupissa muuttujan arvo = ", pysyluupissa)
        print("data type of true is ", type(True))

xakseli, yakseli = makeSignal()  # this function returns 2 parameters
plot(xakseli, yakseli)           # this function call does not return anything.
#loopfunction()