#!/usr/bin/env python3
#-*- coding:utf-8 -*-

'type'

__author__ = 'HUA'

print('type(123) = ', type(123))
print('type(\'123\') = ', type('123'))
print('type(None) = ', type(None))
print('type(abs) = ', type(abs))

import types

print('type(\'abc\') == str ? ', type('abc') == str)
print('isinstance(\'abc\',str) ? ', isinstance('abc', str))
