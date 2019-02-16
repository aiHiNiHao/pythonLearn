import threading
import time

def function():
    print("function start")
    time.sleep(1)
    print("function end")


print("Main Thread Start")
thread = threading.Thread(target=function, args=())
thread.start()
print("Main Thread End")