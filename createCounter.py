# -*- coding:utf-8 -*-
#利用闭包返回一个计数器函数，每次调用它返回递增整数：
def createCounter():
    n = [0]

    def counter():
        n[0] = n[0] + 1
        return n[0]

    return counter


counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA())
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')