
queue = []

def counter():
    count = 0
    while True:
        print(count)
        count += 1
        yield 

def printer():
    count = 0
    while True:
        if count % 3 == 0:
            print('Bang! ')
            count += 1
        yield



def main():
    while True:
        q = queue.pop(0)
        next(q)
        queue.append(q)


if __name__ == '__main__':
    q1 = counter()
    queue.append(q1)
    q2 = printer()
    queue.append(q2)
    main()