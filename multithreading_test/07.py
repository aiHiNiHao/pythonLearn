import time
import threading

def function():
    print("Function Start")
    time.sleep(1)
    print("Function End")

print("Main Thread Start|")

thread = threading.Thread(target=function, args=())
thread.setDaemon(True)# 设为守护线程后，主线程执行完，该线程就被粗鲁的结束
thread.start()

print("Main Thread End")
