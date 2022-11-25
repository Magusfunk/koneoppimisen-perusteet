import matplotlib.pyplot as plt
import numpy as np

M = 100
x = np.linspace(50,300,M)
y = x*1000 + 100000*np.random.random([M,])
x = 5*np.random.randn(M)
y = x**2 + 5*np.random.randn(M)

c = np.random.randn(1)
b = np.random.randn(1)
a = np.random.randn(1)

c_adjusted_values = np.empty(0)
b_adjusted_values = np.empty(0)
a_adjusted_values = np.empty(0)
rate = 0.00003  

plt.figure(1)
for rounds in range(100):
    grad_c = 0
    grad_b = 0
    grad_a = 0
    print(M)
    for i in range(M):
        grad_c = grad_c + (a*x[i]**2 + b*x[i] + c - y[i]) * 1
        grad_b = grad_b + (a*x[i]**2 + b*x[i] + c - y[i]) * x[i]
        grad_a = grad_a + (a*x[i]**2 + b*x[i] + c - y[i]) * x[i]**2
    c = c - (rate/(M*1.0))*grad_c
    b = b - (rate/(M*1.0))*grad_b
    a = a - (rate/(M*1.0))*grad_a
    c_adjusted_values = np.append(c_adjusted_values,c)
    b_adjusted_values = np.append(b_adjusted_values,b)
    a_adjusted_values = np.append(a_adjusted_values,a)
    

    xmin = np.min(x)
    xmax = np.max(x)
    x1 = np.linspace(xmin,xmax,100)
    h = a*(x1**2) + b*x1 + c

    plt.subplot(2,2,1)
    plt.plot(c_adjusted_values,'-*b')
    plt.title('Adjusted c values')

    plt.subplot(2,2,2)
    plt.plot(b_adjusted_values,'-*g')
    plt.title('Adjusted b values ')

    plt.subplot(2,2,3)
    plt.plot(a_adjusted_values,'-*g')
    plt.title('Adjusted a values ')

    plt.subplot(2,2,4)
    #plt.clf()
    plt.plot(x,y,'.r')
    plt.plot(x1, h, '-b')
    plt.title('Known datapoints and fitting straight line')
    plt.pause(0.001)

plt.show()
