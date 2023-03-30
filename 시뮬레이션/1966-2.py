from collections import deque

import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    s = list(map(int, input().split()))
    q = deque()
    for i, x in enumerate(s):
        q.append((i, x))
    s.sort()
    cnt = 0
    while q:
        i, x = q.popleft()
        if x == s[-1]:
            s.pop()
            cnt += 1
            if i == m:
                print(cnt)
                break
        else:
            q.append((i, x))
