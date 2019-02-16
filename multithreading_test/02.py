import time
import _thread as thread

def loop1():
    print("loop1 start", time.ctime())
    time.sleep(3)
    print("loop1 end ", time.ctime())

def loop2():
    print("loop2 start", time.ctime())
    time.sleep(1)
    print("loop2 end ", time.ctime())

def main():
    thread.start_new_thread(loop1,())
    thread.start_new_thread(loop2, ())

if __name__ == '__main__':
    main()
    while True:
        time.sleep(1)