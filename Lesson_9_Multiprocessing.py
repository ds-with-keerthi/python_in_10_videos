# Libraries
import multiprocessing
import time

# Functions
def rice_making():
    print("Making RICE: wash rice \n")
    print("Making RICE: soak rice \n")
    time.sleep(2)
    print("Making RICE: cook in cooker \n")
    time.sleep(2)

def sambar_making():
    print("Making SAMBAR: cut and cook veges\n")
    time.sleep(2)
    print("Making SAMBAR: cook paruppu \n")
    time.sleep(2)
    print("Making SAMBAR: mix veges + paruppu\n")
# # Time before multiprocessing
# start = time.time()
# rice_making()
# sambar_making()
# end =time.time()

# print("Total time : ", end-start)

if __name__ == '__main__':

    # Time after multiprocessing
    process_1 = multiprocessing.Process(target=rice_making)
    process_2 = multiprocessing.Process(target=sambar_making)


    start = time.time()
    # start process
    process_1.start()
    process_2.start()

    # end process
    process_1.join()
    process_2.join()
    end = time.time()

    print("Total time : ", end-start)


import multithreading

