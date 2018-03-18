# encoding: utf-8

'''

@author: ZiqiLiu


@file: RWLOCK2.py

@time: 2018/3/17 下午10:29

@desc:
'''
import threading


# this version will favor writer, which might cause starvation of reader

class RWLock:
    def __init__(self):
        self.rmutex = threading.Semaphore()
        self.wmutex = threading.Semaphore()
        self.wlock = threading.Semaphore()
        self.rlock = threading.Semaphore()
        self.read_cnt = 0
        self.write_cnt = 0

    def r_acquire(self):
        self.rlock.acquire()
        self.rmutex.acquire()
        self.read_cnt += 1
        if self.read_cnt == 1:
            # first reader, acquire write lock
            self.wlock.acquire()
        self.rmutex.release()
        self.rlock.release()

    def r_release(self):
        self.rmutex.acquire()
        self.read_cnt -= 1
        if self.read_cnt == 0:
            self.wlock.release()
        self.rmutex.release()

    def w_acquire(self):
        self.wmutex.acquire()
        self.write_cnt += 1
        if self.write_cnt == 1:
            self.rlock.acquire()
        self.wmutex.release()

        self.wlock.acquire()

    def w_release(self):
        self.wlock.release()

        self.wmutex.acquire()
        self.write_cnt -= 1
        if self.write_cnt == 0:
            self.rlock.release()
        self.wmutex.release()
