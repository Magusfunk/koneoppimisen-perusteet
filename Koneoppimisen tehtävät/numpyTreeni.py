import numpy as np
nimi = "mika mikkeli"
print(nimi.title())


lista = np.arange(1,10,dtype=np.float32).reshape(3,3)
print(lista)
print(lista.dtype) #Muuttujan tyypii
print(lista.ndim) #Ulottuvuuksien määrä
print(lista.size) #Listan alkioiden määrä
print(lista.shape) #Listan rivien ja sarakkadein määrä

nollia = np.zeros((2,10))
print(nollia)

askelLista = np.arange(0,11,2) #Alku, loppu, askel
print(askelLista)

väliLista = np.linspace(0,100,101) #Alku, loppu, jakojen määrä
print(väliLista)

a = np.array([[2,2],[2,2]])
b = np.array([[2,4],[6,8]])
print(np.dot(a,b))
print(a*b)

# print(lista.reshape(1,9))
# print(lista.ravel)


# for row in lista:
#     print(row)

# for cell in lista.flat:
#     print(cell)