#!/usr/bin/env python3
# -*- coding: utf-8 -*-

L = (x*x for x in range(10))
print(L)

#-------------------------

def fib(max):
    n, a, b = 0, 0, 1
    while n<max:
        yield b
        a , b = b, a+b
        n = n+1
    return 'done'
for y in fib(6):
    print(y)


#----------------------
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)

o = odd()
next(o)
next(o)
next(o)

#-------------------------
def triangles():
    L = [1]
    while True:
        yield L
        L = [1] + [L[i]+L[i+1] for i in range(len(L)-1)] +[1]

n=0
result =[]
for t in triangles():
    result.append(t)
    n = n+1
    if n==10:
        break

for x in result:
    print(x)