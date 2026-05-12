# import time
# import multiprocessing

# def do_something():
#     print("Doing something ....")
#     time.sleep(1)
#     print("Finished ...")

# t1 = time.perf_counter()
# # do_something()
# # do_something()

# p1 = multiprocessing.Process(target=do_something)
# p2 = multiprocessing.Process(target=do_something)

# p1.start()
# p2.start()

# p1.join()
# p2.join()

# t2 = time.perf_counter()
# print(f"Executed in {round(t2-t1, 3)} seconds")


# import time
# import multiprocessing
# import os

# def do_something():
#     print(f"Doing something .... {os.getpid()}")
#     time.sleep(1)
#     print(f"Finished ... {os.getpid()}")

# t1 = time.perf_counter()

# processes = []
# for i in range(10):
#     p = multiprocessing.Process(target=do_something)
#     p.start()
#     processes.append(p)


# for p in processes:
#     p.join()

# t2 = time.perf_counter()
# print(f"Executed in {round(t2-t1, 3)} seconds")

# import time
# import os
# import concurrent.futures

# def do_something(seconds):
#     print(f"Doing something .... {os.getpid()}")
#     time.sleep(seconds)
#     return f"Finished ... seconds = {seconds}, {os.getpid()}"

# t1 = time.perf_counter()
# with concurrent.futures.ProcessPoolExecutor() as executor:
#     secs = [5, 4, 3, 2, 1]
#     tasks = [executor.submit(do_something, sec) for sec in secs]
#     for i in concurrent.futures.as_completed(tasks):
#         print(i.result())

# t2 = time.perf_counter()
# print(f"Executed in {round(t2-t1, 3)} seconds")


import time
import os
import concurrent.futures

def do_something(seconds):
    print(f"Doing something .... {os.getpid()}")
    time.sleep(seconds)
    return f"Finished ... seconds = {seconds}, {os.getpid()}"

t1 = time.perf_counter()
with concurrent.futures.ProcessPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1]
    tasks = executor.map(do_something, secs)
    for i in tasks:
        print(i)

t2 = time.perf_counter()
print(f"Executed in {round(t2-t1, 3)} seconds")
