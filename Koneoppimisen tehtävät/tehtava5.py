'''
Install scikit-learn module with pip install scikit-learn command.

Tehtävät:
1. Luetaan dataout.csv tiedosto pandas data frameksi siten, että tiedostosta luetaan vai
   sarakkeet xyz ja labels. Eli jätetään se indeksi sarake, joka koostuu 0,1,2 jonosta pois. 
   Käytä dataframen read_csv funktiota ja sieltä parametreja delimiter=, header=, usecols=

2. Poistetaan edellä luetusta dataframesta sen ensimmäinen rivi, jossa siis xyz ja labels tieto.
   Tämä siksi, että jäljelle jäänyttä 60,3 matriisia ja string saraketta käytetään eri algoritmien
   opettamiseen. Käytä dataframe iloc metodia

3. Seuraavaksi suodatetaan dataframesta pois sellaiset rivit, joissa x,y tai z arvo on suurempi
   kuin 1023, mikä on Arduinon analogia muuntimen maksimi lukema. Eli poistetaan virheelliset 
   mittaustulokset. Tulosta dataframe rivistä 40 eteenpäin (iloc käsky) ennen suodatusta ja 
   suodatuksen jälkeen, jotta varmistut siitä, että osa riveistä poistuu suodatuksen avulla
   Selvitä internetin avulla kuinka pandas dataframen sarakkeen arvoja voi suodattaa.

4. Seuraavaksi irroitetaan dataframesta labels tiedot left, right, up ja down tietoja
   kertova sarake (sen pitäisi olla neljäs sarake. Voit kokeilla esim print(df[4]) komennolla)
   Muutetaan sarakkeen tyyppi as_type komennolla 'category' tyypiksi ja luodaan dataframeen
   vielä viides sarake ja alustetaan sinne df[4].cat.codes funktion avulla numeeriset arvot
   left, rigth, up ja down arvoja vastaamaan.

5. Seuraavaksi "irroitetaan" dataframesta x,y,z sarakkeet ja muodostetaan niistä yksi 
   NumPy array, jossa on kolme saraketta ja N kpl rivejä. Tämä array = matriisi = data on sitten
   se, mitä käytetään eri mallien datana opettamiseen. Irroitetaan myös numpy arrayksi
   se viides sarake joka edellisessä vaiheessa saatiin tehtyä. Ja tätä käytetään opetuksessa
   kertomaan, mitä kukin data matriisin rivi edustaa = labels. Ja muutetaan molemmat irroitetut
   data ja labels int tyyppisiksi.

6. Ja nyt vihdoin data on käsitelty algoritmin opettamiseen sopivaksi. Jaetaan data vielä
   training ja test datasetteihin ja käytetään siihen sklearn kirjaston train_test_split luokkaa
   jonka voi importata komennolla from sklearn.model_selection import train_test_split. Tee
   sellainen jako, että datasta 20% jätetään testaukseen ja 80% datasta käytetään opetukseen.
   Netistä löytyy taas hyviä esimerkkejä, miten tämä tehtään: https://realpython.com/train-test-split-python-data/

7. Ja lopuksi testataan random forest ja K-means algoritmien toimivuutta. Eli opetetaan opetusdatalla
   x_train,y_train sekä random forest että K-means malli. Ja sen jälkeen testataan mallin tarkkuus
   x_test,y_test datalla. Ja ylimääräisenä tehtävänä voi vielä mitata kummastakin algoritmista kuinka
   kauaan mallin opettaminen kestää ja kuinka kauan yhden ennustuksen tekeminen mallilla kestää. Ja
   apuja löytyy taas netistä seuraavasti:
   K-means: https://towardsdatascience.com/knn-using-scikit-learn-c6bed765be75
   Random Forests:https://www.datacamp.com/tutorial/random-forests-classifier-python
       
'''

import sklearn # This is anyway how package is imported
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import time

#Datan importaus
filename = "C:/temp/koneoppimisen-perusteet/koodit/Koneoppimisen tehtävät/dataout.csv"
data = pd.read_csv(filename,usecols=[1,2,3,4],delimiter='\t',header=0)
df = pd.DataFrame(data)

#Datan suodatus ja käsittely
dfSuodatus = df[(df.x < 1024) & (df.y < 1024) & (df.z < 1024)]
dfSuodatus['category'] = df['labels'].astype('category').cat.codes
xyz = dfSuodatus.iloc[:,0:3].to_numpy()
xyz = xyz.astype('int')
labels = dfSuodatus['category'].to_numpy()
labes = labels.astype('int')

#Datan jako testi ja treenidataan
xyz_train, xyz_test, labels_train, labels_test = train_test_split(xyz, labels,test_size=0.2)
xyz_test = np.asarray(xyz_test)
xyz_train = np.asarray(xyz_train)
labels_test = np.asarray(labels_test)
labels_train = np.asarray(labels_train)


#KNN mallin sovitus ja tulosten tarkastelu
knn = KNeighborsClassifier(n_neighbors=10)
start = time.time()
knn.fit(xyz_train,labels_train)
print("KNN mallin opetus kesti: ",(time.time()-start)*1000,"Ms")
start = time.time()
KNN_predict = knn.predict(xyz_test)
print("KNN mallin ajaminen kesti: ",(time.time()-start)*1000,"Ms")
print(labels_test, ": Testidata KNN")
print(KNN_predict, ": Ennustedata KNN")
print("KNN mallin tarkkuus: ",metrics.accuracy_score(labels_test,KNN_predict))

#Random forest mallin sovitus ja tulosten tarkastelu
rForest = RandomForestClassifier(n_estimators=100)
start = time.time()
rForest.fit(xyz_train,labels_train)
print("rForest mallin opetus kesti: ",(time.time()-start)*1000,"Ms")
start = time.time()
rForestPredict = rForest.predict(xyz_test)
print("rForest mallin ajaminen kesti: ",(time.time()-start)*1000,"Ms")
print(labels_test, ": Testidata rForest")
print(rForestPredict, ": Ennustedata rForest")
print("Random Forest mallin tarkkuus:",metrics.accuracy_score(labels_test,rForestPredict))