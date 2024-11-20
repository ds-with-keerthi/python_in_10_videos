from concurrent.futures import ThreadPoolExecutor
import time

def find_cube_value(num):
    time.sleep(2)
    return num *  num * num

if __name__== '__main__':
    start=time.time()
    with ThreadPoolExecutor(max_workers=3) as executer:
        res = executer.map(find_cube_value, [1,2,3,4,5])
    end = time.time()

    print(end-start)

    for i in res:
        print(i)

