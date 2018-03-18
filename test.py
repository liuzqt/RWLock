# encoding: utf-8

'''

@author: ZiqiLiu


@file: test.py

@time: 2018/2/19 下午10:42

@desc:
'''
from RWLOCK import RWLock as rwlock1
from RWLOCK2 import RWLock as rwlock2
import time
import threading

lock = rwlock2()


def read(tid):
    lock.r_acquire()
    print('thread %d is reading...' % tid)
    time.sleep(2)
    print('thread %d finish reading')
    lock.r_release()


def write(tid):
    lock.w_acquire()
    print('thread %d is writing...' % tid)
    time.sleep(2)
    print('thread %d finish writing' % tid)
    lock.w_release()


if __name__ == '__main__':
    jobs = ['r', 'r', 'w', 'r', 'r', 'w']
    ts = []
    for i, j in enumerate(jobs):
        if j == 'r':
            t = threading.Thread(target=read, args=(i,))
        else:
            t = threading.Thread(target=write, args=(i,))
        t.start()
        ts.append(t)
    for t in ts:
        t.join()
