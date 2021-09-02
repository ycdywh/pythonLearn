# 服务进程在windows系统和Linux系统上有所不同
# 创建一个分布式进程：包括服务进程和任务进程
# 多个进程之间的通信使用Queue
# 该代码为服务进程
# 注意，运行时先运行服务进程，再运行任务进程
# 任务执行循序：
# 服务进程和任务进行都创建了相同的两个队列，一个用来放任务，一个用来放结果
# 第一步：服务进程运行，比如将数字2放进任务队列，任务进程从任务队列中取出数字2
# 第二步：取出数字，执行任务，就是2*2=4, 任务执行完后，放进结果队列
# 第三步：服务进程从结果队列中，取出结果。
# 第四步：所有任务执行完毕，所有结果都已经取出，最终任务队列和结果队列都是空的了

# -*- coding:utf-8 -*-
import random, queue
from multiprocessing.managers import BaseManager
from multiprocessing import freeze_support

# 第一步：定义两个Queue队列，一个用于发送任务，一个接收结果
task_queue = queue.Queue()
result_queue = queue.Queue()
# 创建类似的QueueManager,继承BaseManager,用于后面创建管理器
class QueueManager(BaseManager):
    pass
# 定义两个函数，返回结果就是Queue队列
def return_task_queue():
    global task_queue # 定义成全局变量
    return task_queue # 返回发送任务的队列
def return_result_queue():
    global result_queue
    return result_queue # 返回接收结果的队列

# 第二步：把上面创建的两个队列注册在网络上，利用register方法
# callable参数关联了Queue对象，将Queue对象在网络中暴露
# 第一个参数是注册在网络上队列的名称
def test():
    QueueManager.register('get_task_queue', callable=return_task_queue)
    QueueManager.register('get_result_queue', callable=return_result_queue)

    # 第三步：绑定端口5000，设置验证口令,这个相当于对象的初始化
    # 绑定端口并填写验证口令，windows下需要填写IP地址，Linux下默认为本地，地址为空
    manager = QueueManager(address=('127.0.0.1', 8001), authkey=b'abc') # 口令必须写成类似b'abc'形式，只写'abc'运行错误

    # 第四步：启动管理器，启动Queue队列，监听信息通道
    manager.start()

    # 第五步：通过管理实例的方法获访问网络中的Queue对象
    # 即通过网络访问获取任务队列和结果队列,创建了两个Queue实例，
    task = manager.get_task_queue()
    result = manager.get_result_queue()
    # 第六步：添加任务，获取返回的结果
    # 将任务放到Queue队列中
    for i in range(10):
        n = random.randint(0, 10) # 返回0到10之间的随机数
        print("Put task %s ..." % n)
        task.put(n) # 将n放入到任务队列中
    # 从结果队列中取出结果
    print("Try get results...")
    for i in range(11): # 注意，这里结果队列中取结果设置为11次，总共只有10个任务和10个结果，第10次用量确认队列中是不是已经空了
        # 总共循环10次，上面放入了10个数字作为任务
        # 加载一个异常捕获
        try:
            r = result.get(timeout=5) # 每次等待5秒，取结果队列中的值
            print("Result: %s" % r)
        except queue.Empty:
            print("result queue is empty.")

    # 最后一定要关闭服务，不然会报管道未关闭的错误
    manager.shutdown()
    print("master exit.")

if __name__ == '__main__':
    # Windows下多进程可能出现问题，添加以下代码可以缓解
    freeze_support()
    print("Start!")
    # 运行服务进程
    test()
