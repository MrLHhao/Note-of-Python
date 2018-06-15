import random

i = 0
time = int(input('how many times do you want:'))


def ran():
    times = random.randint(1, 20)
    i = 0
    while i < times:
        x = random.randint(1, 35)
        i += 1
    return x


def ran1():
    times = random.randint(1, 20)
    i = 0
    while i < times:
        x = random.randint(1, 12)
        i += 1
    return x


while i < time:
    while True:
        a = ran()
        b = ran()
        if a != b:
            break
    while True:
        c = ran()
        if c == a or c == b:
            continue
        break
    while True:
        d = ran()
        if d == a or d == b or d == c:
            continue
        break
    while True:
        e = ran()
        if e == a or e == b or e == c or e == d:
            continue
        break
    while True:
        f = ran1()
        g = ran1()
        if f != e:
            break
    list1 = sorted([a, b, c, d, e])
    list2 = sorted([f, g])
    print('The Winning Number is ', '{0}+{1}.'.format(list1, list2))
    i += 1
print('Winner Winner Chicken Dinner!')
