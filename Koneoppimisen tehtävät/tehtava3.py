import numpy as np
import matplotlib.pyplot as plt
import sys
import time



''' Let's prove 3 things where NumPy is better than just Python data structures

1) Numpy requires less memory
2) Numpy is faster
3) Numpy is convenient '''

N = 100000
pythonList = range(N)
# as all python list elements are objects we can calculate memory
# size of a Python list as follows (number of elements * element size)
print("Python list size = ", len(pythonList)*sys.getsizeof(1))

''' Your task is to first create N element wide NumPy list, then
calculate and print NumPy list size. Hint. use size and itemsize attributes of 
NumPy '''

numpyList = np.arange(N)
print("NumPy list size = ", numpyList.size*numpyList.itemsize)

# And now we demonstrate that NumPy is faster
# Let's multiply lists generated by themselves
start = time.time()
pythonListResult = [(x+y) for x,y in zip(pythonList,pythonList)]
print("Adding each element in a Python list took =",(time.time()-start)*1000,"ms")
for x in range(3):
   print (pythonList[x])
print(pythonListResult[0:3])

# Let's multiply lists generated by themselves
start = time.time()
numpyListResult = numpyList + numpyList
print("Adding each element in a Numpy list took =",(time.time()-start)*1000,"ms")

start = time.time()
count = 0
pythonNewResultList = []
while(count < len(pythonList)):
       pythonNewResultList.append(pythonList[count] + pythonList[count])
       count += 1
print("Adding each element in a new Python list took =",(time.time()-start)*1000,"ms")

plt.figure(1,figsize=(10,5))
plt.subplot(311)
plt.title("Python list result")
plt.plot(pythonListResult)
plt.subplot(312)
plt.title("Numpy list result")
plt.plot(numpyListResult)
plt.subplot(313)
plt.title("New python list result")
plt.plot(pythonNewResultList)
plt.subplots_adjust(hspace=0.5)

plt.show()

# Numpyllä listojen käyttö on paljon helpompaa ja nopeampaa. Ne käyttää vähemmän muistia. Lisäksi numpyn listoilla on käteviä metodeja jotka helpottaa niiden käsittelyä
# merkittävästi.

'''
Your tasks are the following:
1) prove to yourself that line 33 actually does element by element addition
2) use some other Python looping function to implement python list element by element
   addition and measure its time
3) Implement NumPy list addition without for loop (as NumPy can do vector and matrix
   additions without a loop function). And measure NumPy list addition time
4) plot (with help of plt.subplot) 3 results 1) python list addition result,
   2) your own loop addition result and 3) NumPy list addition result to one figure
   and of course all 3 results should be the same
5) Explain in a comment of your python file why NumPy is convenient (mukava)
'''