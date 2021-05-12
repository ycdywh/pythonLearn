#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections.abc import Iterable,Iterator
if isinstance([],Iterable):
    print(True)
if isinstance((x for x in range(10)),Iterable):
    print(True)
if isinstance({},Iterable):
    print(True)
if isinstance('abc',Iterable):
    print(True)

if isinstance('abc',Iterator):
    print(True)
else:
    print(False)

if isinstance(iter('abc'),Iterator):
    print(True)