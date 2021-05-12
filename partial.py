#-*- coding:utf-8 -*-
import functools

int2 = functools.partial(int, base=2)

print('1000000 = ', int2('1000000'))
print('1010101 = ', int2('1010101'))


def add(a,b,c):
    print(a+b+c)
add2 = functools.partial(add,b=2)

add2(1,c=3)
