# encoding: utf-8

'''

@author: ZiqiLiu


@file: RWLOCK.py

@time: 2018/3/17 下午10:21

@desc:
'''
import threading


# this version will favor reader, which might cause starvation of writer

def _mutex(func):
    def wrapper(*args, **kw):
        self = args[0]
        self.mutex.acquire()
        res = func(*args, **kw)
        self.mutex.release()
        return res

    return wrapper


class RWLock:
    def __init__(self):
        self.mutex = threading.Semaphore()
        self.wlock = threading.Semaphore()
        self.read_cnt = 0

    @_mutex
    def r_acquire(self):

        self.read_cnt += 1
        if self.read_cnt == 1:
            # first reader, acquire write lock
            self.wlock.acquire()

    @_mutex
    def r_release(self):
        self.read_cnt -= 1
        if self.read_cnt == 0:
            self.wlock.release()

    def w_acquire(self):
        self.wlock.acquire()

    def w_release(self):
        self.wlock.release()
