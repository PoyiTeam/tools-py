import multiprocessing as mp
import os


def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())


def f(name):
    info('function f')
    print('hello', name)


def multi_process(name):
    if __name__ != '__main__':
        info('single process')
        p = mp.Process(target=f, args=[name])
        p.start()
        p.join()
