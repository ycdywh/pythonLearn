#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def test(n):
    return lambda x : x%n >0

it = [1,2,3,4,5,6,7,8,9,0]
result = filter(test(2),it)
print(list(result))