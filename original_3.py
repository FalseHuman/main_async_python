from time import time


def gen1(s):
    for i in s:
        yield i

def gen2(s):
    for i in range(s):
        yield i

def gen_filename():
    while True:
        pattern = 'file_{}.jpg'
        t = int(time() + 1000)

        yield pattern.format(str(t))

        sum_number = 100 + 100 # Работает при следующей итерации цикла
        print(sum_number)

# Принцип round robin на генераторах
g1 = gen1('emil')
g2 = gen2(10)

tasks = [g1, g2]

while tasks:
    task = tasks.pop(0)

    try:
        i = next(task)
        print(i)
        tasks.append(task)
    except StopIteration:
        pass