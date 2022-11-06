import math
import time


def getDist(p1, p2):
    x2 = math.pow(p1[0]-p2[0], 2)
    y2 = math.pow(p1[1]-p2[1], 2)
    return math.sqrt(x2+y2)


def find_min_distance(a, split='x'):
    if len(a) == 1 or len(a) == 0:
        return -1
    if len(a) == 2:
        return getDist(a[0], a[1])
    if len(a) == 2:
        d1 = getDist(a[0], a[1])
        d2 = getDist(a[1], a[2])
        d3 = getDist(a[2], a[0])
        return min(min(d1, d2), d3)
    group1 = []
    group2 = []
    group3 = []
    if split == 'x':
        axis = 0
        next_axis = 'y'
    else:
        axis = 1
        next_axis = 'x'

    center = (a[0][axis]+a[1][axis])/2
    for p in a:
        if p[axis] < center:
            group1.append(p)
        else:
            group2.append(p)
    m1 = find_min_distance(group1, split=next_axis)
    m2 = find_min_distance(group2, split=next_axis)
    d = max(m1, m2)
    for p in a:
        if (center-d) < p[axis] < (center+d):
            group3.append(p)
    m3 = find_min_distance_brutal(group3)
    if m1 == -1:
        m1 = 1000000
    if m2 == -1:
        m2 = 1000000
    if m3 == -1:
        m3 = 1000000
    return min(min(m1, m2), m3)


data = []
number = int(input('개수:'))
for _ in range(number):
    x, y = input('좌표:').split()
    x = int(x)
    y = int(y)
    data.append((x, y))
t1 = time.time()
dist = find_min_distance_brutal(data)
t2 = time.time()
print('brutal:', dist, t2-t1)
t1 = time.time()
dist = find_min_distance(data)
t2 = time.time()
print('divide:', dist, t2-t1)
