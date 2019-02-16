import time
import threading

def loop1(name):
    print("loop1, start  name = {}".format(name), time.ctime())
    time.sleep(3)
    print("loop1 end name = {}".format(name), time.ctime())

def loop2(name, age):
    print("loop2, start  name = {}, age = {}".format(name, age), time.ctime())
    time.sleep(1)
    print("loop2 end name = {}, age = {}".format(name, age), time.ctime())

def main():

    print("Starting at:", time.ctime())
    thread1 = threading.Thread(target=loop1, args=("xiaoli",))
    thread1.start()
    thread2 = threading.Thread(target=loop2, args=("lijing", 24))
    thread2.start()
    print("end at:", time.ctime())

if __name__ == '__main__':
    main()

