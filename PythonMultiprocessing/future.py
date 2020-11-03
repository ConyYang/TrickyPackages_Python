import concurrent.futures
import time

start = time.perf_counter()


def do_something(sleep_time):
    print('Start sleeping for {} second'.format(sleep_time))
    time.sleep(sleep_time)
    return f'Done Sleeping...{sleep_time}'


def normal_declare():
    with concurrent.futures.ProcessPoolExecutor() as executor:
        f1 = executor.submit(do_something, 1)
        f2 = executor.submit(do_something, 1)
        print(f1.result())
        print(f2.result())


def loop_declare():
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = [executor.submit(do_something, 1) for _ in range(10)]

        for f in concurrent.futures.as_completed(results):
            print(f.result())


def user_define_second():
    with concurrent.futures.ProcessPoolExecutor() as executor:
        secs = [5, 4, 3, 2, 1]
        results = [executor.submit(do_something, sec) for sec in secs]

        for f in concurrent.futures.as_completed(results):
            print(f.result())


def map_user_define_second():
    with concurrent.futures.ProcessPoolExecutor() as executor:
        secs = [5, 4, 3, 2, 1]
        results = executor.map(do_something, secs)
        for r in results:
            print(r)


map_user_define_second()
finish = time.perf_counter()
time_elapse = finish - start
print('Program finished in {} second(s)'.format(time_elapse))
