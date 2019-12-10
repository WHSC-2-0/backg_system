import time


# 当前时间
def add_time():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

print(add_time(), len(add_time()))