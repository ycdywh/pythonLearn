# -*- coding:utf-8 -*-
import functools


def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print("%s %s" % (text, func.__name__))
            return func(*args, **kw)

        return wrapper

    return decorator


@log('execute')
def now():
    print('2020-08-26')


now()
print(now.__name__)

#-------------------------------------------------
#请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间
import time, functools


def logT(text):
    if isinstance(text,str):
        def decorator(fn):
            @functools.wraps(fn)
            def wrapper(*args, **kw):
                startTime = time.time()
                print("日志：%s" % text)
                print("%s start time %s" % (fn.__name__, startTime))
                f = fn(*args, **kw)
                endTime = time.time()
                print("%s end time %s" % (fn.__name__, endTime))
                return f

            return wrapper

        return decorator
    else:
        @functools.wraps(text)
        def wrapper(*args, **kw):
            startTime = time.time()
            print("日志：%s" % text)
            print("%s start time %s" % (text.__name__, startTime))
            f = text(*args, **kw)
            endTime = time.time()
            print("%s end time %s" % (text.__name__, endTime))
            return f

        return wrapper


#测试
@logT
def fast(x, y):
    time.sleep(0.0012)
    return x + y


@logT('111111111')
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z


f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')
