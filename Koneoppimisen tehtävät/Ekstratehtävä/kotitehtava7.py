'''
Tehtävät:
1. Lue kuva4.csv tiedosto pandas kirjaston avulla ja muuta se numpy arrayksi esimerkin mukaisesti

2. Selvitä, minkä kokoinen kuva on ja muokkaa siitä 28x28 pikselin kokoinen kuva, jonka tulostat
   matplotlib kirjaston plt.imshow -komennolla.

3. Selvitä internetistä, kuinka sigmoid funktio voidaan toteuttaa pythonilla ja numpyllä. Tee siitä 
   aliohjelma ja testaa sen toiminta syöttämällä aliohjelmaan sisälle numpy array, jossa 100 kpl
   arvoja -20 ja +20 väliltä. Käytä np.linspace -funktiota tuon datan tekemiseen. Ja lopuksi tulosta
   kuva plt.plot(x,y) -komennolla, missä x = tekemäsi input data ja y = sigmoid funktiosi output.

4. Selvitä (anna opettajan kertoa), miten 784,30,10 -kokoisen neuroverkon output lasketaan. Toteuta tuo laskenta
   numpyn matmul -komentoa ja tekemääsi sigmoid funktiota hyödyntäen. Saat opetetun neuroverkon parametrit w1,w2
   b1, b2 luettua vastaavista csv tiedostoista. Ja lopuksi tulosta neuroverkon kuvasta 4 laskema tulos.

'''

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def sigmoid(x): # tähän voit toteuttaa sigmoid funktiosi.
   y = 1 / (1 + np.exp(-x))
   return y
   
x = np.linspace(-20,20,100)
y = sigmoid(x)


df = pd.read_csv('C:/temp/koneoppimisen-perusteet/koodit/Koneoppimisen tehtävät/Ekstratehtävä/kuva4.csv',header=None)  # näin saadaan luettua kaikki rivit
a0 = df.to_numpy()                                                                                                     # activation a0 tätä voidaan käyttää neuroverkon inputtina
kuva = df.to_numpy();                                                                                                  # Ja tätä voit sitten muokata kuvan tulostamiseksi
a0 = a0.flatten() 

df = pd.read_csv('C:/temp/koneoppimisen-perusteet/koodit/Koneoppimisen tehtävät/Ekstratehtävä/w1.csv',header=None)     # Tästä tiedostosta luetaan opetetut painokertoimet
w1 = df.to_numpy()                                                                                                     # w1 = 30x784 matriisi

df = pd.read_csv('C:/temp/koneoppimisen-perusteet/koodit/Koneoppimisen tehtävät/Ekstratehtävä/w2.csv',header=None)     # Tästä tiedostosta luetaan opetetut painokertoimet
w2 = df.to_numpy()                                                                                                     # w2 = 10*30 matriisi

df = pd.read_csv('C:/temp/koneoppimisen-perusteet/koodit/Koneoppimisen tehtävät/Ekstratehtävä/b1.csv',header=None)     # Tästä tiedostosta luetaan opetetut bias arvot
b1 = df.to_numpy()                                                                                                     # b1 = 30 kpl

df = pd.read_csv('C:/temp/koneoppimisen-perusteet/koodit/Koneoppimisen tehtävät/Ekstratehtävä/b2.csv',header=None)     # Tästä tiedostosta luetaan opetetut bias arvot
b2 = df.to_numpy()                                                                                                     # b2 = 10 kpl

# layer1 = np.empty(30,784)
# for row in w1:
#    layer1 = row * a0

lista = np.arange(-50,50).reshape(4,25)
print(lista)
print(sigmoid(lista))


plt.subplot(311)
plt.plot(x,y)
plt.subplot(312)
plt.imshow(kuva.reshape(28,28))


plt.show()
# cv2.imshow("kuva",kuva.reshape(28,28))
# cv2.waitKey(0)