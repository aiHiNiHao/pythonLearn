import time
import threading

def loop1():
    print("loop1.start")
    time.sleep(1)

def loop2():
    print("loop2.start")
    time.sleep(3)

def loop3():
    print("loop3.start")
    time.sleep(4)


thread1 = threading.Thread(target=loop1, name="111")
thread1.start()
thread2 = threading.Thread(target=loop2, name="222")
thread2.start()
thread3 = threading.Thread(target=loop3, name="333")
thread3.start()

time.sleep(2)
for t in threading.enumerate():
    print(t.getName())