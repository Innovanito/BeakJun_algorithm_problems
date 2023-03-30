'''
1.idea
N,M 을 받고 2째 줄에 순서도를 받는다
큐를 collections에서 import 해온다음
q = deque()로 선언

enumerate로 순서데로 인덱스와 그 값을 i와 x를 생성
그다음 큐에 값을 넣어준다
sort를 해준다음
count 생성

q를 while으로 돌리고
i,x =popleft()에서 sort한 리스트 s=[-1]이 맞으면 
s.pop()
count +1
if i == m이면 print(count)하고 break

sort한게 맞지않으면 append((i,x))

2.시간복잡도
O(N) =100

3.자료구조
n,m 입력값
sort 값 = int[]
queue = q
'''
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
