from multiprocessing import Pool
import os
import time


def main(num):
    pl = Pool()

    __start__ = time.time()

    pl.close()
    pl.join()

    __end__ = time.time() - __start__

    print(f"Processing {len(num)} numbers took {__end__}.")
    print(os.cpu_count())


if __name__ == '__main__':
    num = range(100000000)
    main(num)
