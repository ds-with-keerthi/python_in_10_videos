# Library
import threading
import time

# Functions
def rice_washing():
    print("take bowl\n")
    print("take 2 cup rice\n")
    time.sleep(2)
    print("3 time rinse\n")
    time.sleep(2)

def rice_soaking():
    print("take tumbler\n")
    time.sleep(2)
    print("measure 2 cup water\n")
    time.sleep(2)
    print("put it in rice and soak\n")

# time without multithreading
start = time.time()
rice_washing()
rice_soaking()
end =time.time()

print(end-start)

# time with multithreading
thread_1 = threading.Thread(target=rice_washing)
thread_2 = threading.Thread(target=rice_soaking)

start = time.time()

thread_1.start()
thread_2.start()

thread_1.join()
thread_2.join()

end = time.time()
print(end-start)






