# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1h2J_O_daXG2woTXFDhvFWxpk_h17CzBj
"""

#array method (for the first set of numbers)

import time
import matplotlib.pyplot as plt

def fib(n):
   f = [0] * (n+1)
   f[1] = 1

   for i in range (2,n+1):
      f[i] = f[i-1] + f[i-2]
   return f[n]


x = [5, 7, 10, 12, 15, 17, 20, 22, 25, 27, 30, 32, 35, 37, 40, 42, 45]
y = []

for n in x:
    start = time.time()
    result = fib(n)
    end = time.time()
    y.append(end - start)
    print(f"Fibonacci({n}) = {result}, Time taken: {end - start} seconds")

plt.plot(x, y, marker='o')
plt.title('Array implementation')
plt.xlabel('Input (n)')
plt.ylabel('Time (seconds)')
plt.show()

#array method (for the second set of numbers)

import time
import matplotlib.pyplot as plt

def fib(n):
   f = [0] * (n+1)
   f[1] = 1

   for i in range (2,n+1):
      f[i] = f[i-1] + f[i-2]
   return f[n]

x =[501, 631, 794, 1000,1259, 1585, 1995, 2512, 3162, 3981, 5012, 6310, 7943, 10000, 12589, 15849]
y = []

for n in x:
    start = time.time()
    result = fib(n)
    end = time.time()
    y.append(end - start)
    print(f"Fibonacci({n}) = {result}, Time taken: {end - start} seconds")

plt.plot(x, y, marker='o')
plt.title('Array implementation')
plt.xlabel('Input (n)')
plt.ylabel('Time (seconds)')
plt.show()