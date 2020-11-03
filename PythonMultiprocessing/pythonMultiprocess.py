import multiprocessing
import time

start = time.perf_counter()


def do_something(sleep_time):
    print('Start sleeping for {} second'.format(sleep_time))
    time.sleep(sleep_time)
    print('Done Sleeping...')


def test_1():
    p1 = multiprocessing.Process(target=do_something)
    p2 = multiprocessing.Process(target=do_something)

    p1.start()
    p2.start()
    p1.join()
    p2.join()


processes = []
for _ in range(5):
    p = multiprocessing.Process(target=do_something, args=[1.5])
    p.start()
    processes.append(p)

for process in processes:
    process.join()

finish = time.perf_counter()
time_elapse = finish - start
print('Program finished in {} second(s)'.format(time_elapse))
