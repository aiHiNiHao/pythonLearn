import time
import threading

class FunThread():
    def __init__(self, name):
        self.name = name

    def loop(self, name, nsec):
        print("name == ", name)
        time.sleep(nsec)
        print("end")

def main():

    thread = threading.Thread(target=FunThread("lijing").loop, args = ("Loop1", 1))
    thread.start()

if __name__ == '__main__':
    main()