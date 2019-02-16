import time
import _thread as thread

def loop1(name):
    print("loop1, start  name = {}".format(name), time.ctime())
    time.sleep(3)
    print("loop1 end name = {}".format(name), time.ctime())

def loop2(name, age):
    print("loop2, start  name = {}, age = {}".format(name, age), time.ctime())
    time.sleep(1)
    print("loop2 end name = {}, age = {}".format(name, age), time.ctime())

def main():
    thread.start_new_thread(loop1, ("xiaoli",))
    thread.start_new_thread(loop2, ("lijing", 22))

if __name__ == '__main__':
    main()

    while True:
        time.sleep(1)