import time
import threading

class MyThread(threading.Thread):
    def __init__(self, arg):
        super(MyThread, self).__init__()
        self.arg = arg

    def run(self):
        print("MyThread Start")
        time.sleep(1)
        print("MyThread arg", self.arg)
        print("MyThread end")

thread = MyThread("xiaoli")
thread.start()
thread.join()

print("main thread end")