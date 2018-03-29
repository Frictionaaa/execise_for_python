#计算方法的效率
import cProfile
import random


def func1(ite):
    l1 = sorted(ite)
    l2 = [i for i in l1 if i < 0.5]
    return [i*i for i in l2]


ite = [random.random() for i in range(100000)]

cProfile.run('func1(ite)')

