import numpy as np
import matplotlib.pyplot as plt
'''
Let's look in to matplotlib library properties and train ourselves
with Numpy array manipulations. Your tasks are the following:
1) Make 256*256 pixel picture (instructions given below). Current
   example plots RGB picture where Red component is all ones and G,B components are zero
   thus picture is all red. Your task is to modify picture in such a way that pixels
   at range 0-127 (rows), 0-127 (columns) show red picture area
   at range 0-127 (rows), 128-256 (columns) show green picture area
   at range 128-256 (row), 0-127 (columns) show blue picture area
   at range 128-256 (row), 128-256 (columns) show gray picture area 

'''
size = 256
kuva = np.zeros((size,size,3))
kuva[:,:,0]= np.ones((size,size))
kuva[0:127,128:256] = 0,255,0
kuva[127:256,0:128] = 0,0,255
kuva[127:256,128:256] = 0.5
plt.imshow(kuva)
# plt.show()

'''
Let's look at matplotlib library basic usage tutorials. There is an example
how to create 3 figures as shown below

fig1 = plt.figure()  # an empty figure with no Axes
fig2, ax = plt.subplots()  # a figure with a single Axes
fig3, axs = plt.subplots(2, 2)  # a figure with a 2x2 grid of Axes

Your tasks are the following:
1) create 4 NumPy arrays containing 1 second sine signals with 1, 2, 3, 4 Hz
    HINT:
    create first time t = np.arange(0,1,0.01), where t starts from 0, ends at 0.99
    and then use np.sin and np.pi functions to genereate certain sine signals with certain
    frequencies. And remember the equation = sin(2*pi*f*t)
2) print 1 Hz sine signal to fig1
3) print 2 Hz sine signal to fig2
4) print 1,2,3,4 Hz sine signals to fig3 subplots. HINT: remember that axs is 2*2 matrix. 
   thus accessing second subplot goes with axs[0,1], where 0 = first row, 1 = second column.
5) print titles to all 3 figures
6) change line type and color of line of all 4 subplots at fig3 

7) And finally as we hopefully saw during the lectures that one can put
   many signals to a matrix and then just print matrix and all columns are
   seen as separate signals. Make signal matrix where you have a 1 second 2 Hz sine
   signal and its second power. And print those to a same figure.

'''


t = np.arange(0,1,0.01)
sig1 = np.sin(2*np.pi*1*t)
sig2 = np.sin(2*np.pi*2*t)
sig3 = np.sin(2*np.pi*3*t)
sig4 = np.sin(2*np.pi*4*t)
sig5 = np.power(sig2,2)

signaaliMatriisi = np.zeros((t.size,2))
signaaliMatriisi[:,0] = sig2
signaaliMatriisi[:,1] = sig5

plt.figure(2)
plt.title("Sin 1Hz")
plt.plot(sig1)

plt.figure(3)
plt.title("Sin 2Hz")
plt.plot(sig2)

plt.figure(4)
plt.subplot(221)
plt.title("Sin 1Hz")
plt.plot(sig1,'--g')
plt.subplot(222)
plt.title("Sin 2Hz")
plt.plot(sig2,'+r')
plt.subplot(223)
plt.title("Sin 3Hz")
plt.plot(sig3,'xm')
plt.subplot(224)
plt.title("Sin 4Hz")
plt.plot(sig4,'Dy')
plt.subplots_adjust(hspace=0.4)

plt.figure(5)
plt.title("2Hz + 2Hz^2")
plt.plot(signaaliMatriisi)

sigX = np.sin(2*np.pi*2*t + np.pi/2)
sigY = np.cos(2*np.pi*2*t - np.pi/2)

kompleksiSignaali = complex(2,2)*np.pi*2*t

fig, ax = plt.subplots(subplot_kw=dict(projection='3d'))
ax.plot3D(kompleksiSignaali.real,kompleksiSignaali.imag,t)

plt.show()

''' theta = np.linspace(0, 2*np.pi)
x = np.cos(theta - np.pi/2)
y = np.sin(theta - np.pi/2)
z = theta

fig, ax = plt.subplots(subplot_kw=dict(projection='3d'))
ax.stem(x, y, z)

plt.show() '''