import time
import random
start = time.time()# 记录开始时间
def a(n,age,*args):
    if age>=18:
        print(n)
        for i in args:
            print(i)
    else:
        print("no!")
    return n
time.sleep(a(2,19,7,8,9)/1000)# 使程序暂停 n 毫秒
elapsed_time = time.time() - start# 计算并输出经过的时间
print(elapsed_time)