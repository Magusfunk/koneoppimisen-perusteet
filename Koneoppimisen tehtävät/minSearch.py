import matplotlib.pyplot as plt
import numpy as np

#y = x^2

x = np.linspace(-5,5,100)
y = np.power(x,2)

xArvaus = 10
for i in range(10):
    learningRate = 0.3 
    learningRate = learningRate * 1.5
    derivaatta = 2 * xArvaus
    print(xArvaus,"-",derivaatta * learningRate)
    xArvaus = xArvaus - derivaatta * learningRate
    yArvaus = np.power(xArvaus,2)
    plt.figure(1)
    plt.subplot(5,2,1+i),plt.plot(x,y),plt.plot(xArvaus,yArvaus,'r*')

plt.show()