import threading
def greet():
    print("hello from the thread")
t1 = threading.Thread(target=greet)
t1.start()
def greet2():
    print("hello from the thread 2")
t2 = threading.Thread(target=greet2)
t2.start()
def greet3():
    print("hello from the thread 3")
t3 = threading.Thread(target=greet3)
t3.start()