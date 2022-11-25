'''
 Tämän ja pythonPerusteetMainModule.py tiedoston tavoittena on:
 1) esittää mikä on python moduli
 2) miten tuo moduli = skripti voi toimia itsenäisenä "main" ohjelmana tai olla osa suurempaa kokonaisuutta.
'''

import pythonPerusteetMainModule
from pythonPerusteetMainModule import makeSignal as MS
import matplotlib.pyplot as plt
import numpy as np

def plot(x,y):
    plt.figure(2)
    plt.plot(x,y,'-*')
    plt.show()

x = np.arange(-5,5,0.1)
y = np.power(x,2)
plot(x,y)
#xx,yy = pythonPerusteetMainModule.makeSignal()
#pythonPerusteetMainModule.plot(xx,yy)

xx,yy = MS()
plt.plot(xx,yy)
plt.show()
#pythonPerusteetMainModule.plot(xx,yy)