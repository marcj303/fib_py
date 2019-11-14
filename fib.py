#!/usr/bin/env python3

# Python practice using fibonacci calulations
# Got started here:
# https://medium.com/@TheGeekiestOne/fibonacci-numbers-and-algorithms-to-compute-them-part-2-c3f988ff2203
# Then found some better articles from medium
# https://medium.com/future-vision/fibonacci-sequence-algorithm-5eebae4e85be
# https://towardsdatascience.com/fibonacci-linear-recurrences-and-eigendecomposition-in-python-54a909990c7c
# https://medium.com/@colosi/fibonacci-power-series-and-big-o-f90ca90f0995
# https://www.geeksforgeeks.org/program-for-nth-fibonacci-number/


# Which led to this great info on calculating Fibonacci numbers:
#   http://www.maths.surrey.ac.uk/hosted-sites/R.Knott/Fibonacci/fibFormula.html

#####
import timeit
import numpy as np
import math

# This is a recursive function to calculate a fibonacci number. This function
# is very slow since it calculates each number in the sequence. Python also has
# a lot of overhead for each function call.
def fib(n):
    if n > 1:
        return fib(n-1) + fib(n-2)
    else:
        return n


# This is an itereative array function that uses an array to store each calculation
# in the sequence. We just need to start the first two values in the array.
def fibitar(n):
    a = [0,1]

    if n > 1:
        for i in range(1,n):
            a.append(a[i] + a[i-1])

    return a[n]

# This is an itereative variable function that uses two variable to store each calculation
# in the sequence. We just need to start the first two values in the array. This is faster
# since the variables should stay on the stack and we don't append an array.
def fibitv(n):
    a = 0
    b = 1

    if n > 1:
        for i in range(n):
            # This is a multiple assignment, a = b , b = a+b (a=1, b=1+1)
            a ,b = b, a + b

    return a


# is there a way to do this with an python iterator? It might be faster?


### The following are from the articles above. These use linear algebra, matrix,
### and formulas derived from the basic fibonacci algorythm.

# Using matrix math
def fib_matrix(n):
    Matrix = np.matrix([[0,1],[1,1]])
    vec = np.array([[0],[1]])
    return np.matmul(Matrix**n,vec)

# Note that this is an aproximation and starts to diverge around n == 70.
def fib_formula(n):
    golden_ratio = (1 + math.sqrt(5)) / 2
    val = (golden_ratio**n - (1 - golden_ratio)**n) / math.sqrt(5)
    return int(round(val))

# Using derived fast doubling formula
# F(2n-1) = F(n-1)**2 + F(n)**2
# F(2n) = ( 2 F(n-1) + F(n) ) F(n)

# recursive fast doubleing formula version
def fibrfd(n):
    if n in (0,1):
        return n
    # if n is even
    if n % 2 == 0:
        a = n/2
        b = n/2 - 1
        fa = fibrfd(a)
        fb = fibrfd(b)
        return int(fa * (fa + 2 * fb))
    else:
        #n is odd
        a = (n + 1)/2
        b = (n + 1)/2 - 1
        fa = fibrfd(a)
        fb = fibrfd(b)
        return int(fa * fa + fb * fb)

# itereative fast doubling version
# https://funloop.org/post/2017-04-14-computing-fibonacci-numbers.html
def fibifd(n):
    ns = []
    while n:
        ns.extend([n])
        n >>= 1

    a, b = 0, 1

    while ns:
        n = ns.pop()
        c = a * ((b << 1) - a)
        d = a * a + b * b
        if n & 1:
            a, b = d, c + d
        else:
            a, b = c, d

    return a

# Time and print our functions. Note that the recursive function starts to get big around the
# 30th number, so we use that as the standard.
print("fib(30): ", fib(30), " ", timeit.timeit("fib(30)", setup="from __main__ import fib",number=1))
print("fibitar(500): ", fibitar(500), " ", timeit.timeit("fibitar(500)", setup="from __main__ import fibitar",number=1))
print("fibitv(500): ", fibitv(500), " ", timeit.timeit("fibitv(500)", setup="from __main__ import fibitv",number=1))
print("fib_matrix(500): \n", fib_matrix(500), " ", timeit.timeit("fib_matrix(500)", setup="from __main__ import fib_matrix",number=1))
print("fib_formula(500): ", fib_formula(500), " ", timeit.timeit("fib_formula(500)", setup="from __main__ import fib_formula",number=1))
print("fibrfd(500): ", fibrfd(500), " ", timeit.timeit("fibrfd(500)", setup="from __main__ import fibrfd",number=1))
print("fibifd(500): ", fibifd(500), " ", timeit.timeit("fibifd(500)", setup="from __main__ import fibifd",number=1))
