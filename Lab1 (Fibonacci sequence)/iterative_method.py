# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1h2J_O_daXG2woTXFDhvFWxpk_h17CzBj
"""

# iterative method (first set of numbers)

import time
import matplotlib.pyplot as plt

def fib(n):
    n1 = 0
    n2 = 1
    for _ in range(0 , n):
        n1, n2 = n2, n1 + n2
    return n1

x = [5, 7, 10, 12, 15, 17, 20, 22, 25, 27, 30, 32, 35, 37, 40, 42, 45]
y = []

for n in x:
    start = time.time()
    result = fib(n)
    end = time.time()
    y.append(end - start)
    print(f"Fibonacci({n}) = {result}, Time taken: {end - start:} seconds")

plt.plot(x, y, marker='o')
plt.title('Iterative implementation')
plt.xlabel('Input (n)')
plt.ylabel('Time (seconds)')
plt.show()

# iterative method (second set of numbers)

import time
import matplotlib.pyplot as plt

def fib(n):
    n1 = 0
    n2 = 1
    for _ in range(0 , n):
        n1, n2 = n2, n1 + n2
    return n1

x = [501, 631, 794, 1000, 1259, 1585, 1995, 2512, 3162, 3981, 5012, 6310, 7943, 10000, 12589, 15849]
y = []

for n in x:
    start = time.time()
    result = fib(n)
    end = time.time()
    time_taken = end - start
    y.append(time_taken)
    print(f"Fibonacci({n}) = {result}, Time taken: {time_taken:} seconds")

plt.plot(x, y, marker='o')
plt.title('Iterative implementation')
plt.xlabel('Input (n)')
plt.ylabel('Time (seconds)')
plt.show()