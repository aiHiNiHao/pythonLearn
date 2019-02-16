import time

def loop1():
    print("loop1 start time ",time.ctime())
    time.sleep(1)
    print("loop1 end time ", time.ctime())

def loop2():
    print("loop22222 start time", time.ctime())
    time.sleep(2)
    print("loop22222 end time ", time.ctime())

def main():
    print("starttttt")
    loop1()
    loop2()
    print("enddddddd")

if __name__ == "__main__":
    main()