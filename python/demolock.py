import threading
import time

X = 0
useLock = True

if useLock:
    lock = threading.Lock()

def incr():
    global X
    for _ in range(10):
        if useLock:
            lock.acquire()

        myX = X + 1
        time.sleep(0.01)
        X = myX

        if useLock:
            lock.release()

threads=[]
for i in range(2):
    thread = threading.Thread(target=incr)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

print(X)
