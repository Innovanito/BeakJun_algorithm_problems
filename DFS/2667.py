'''
1. 아이디어
mapSqr 입력 받고 방문 여부 chk를 확인한 다음에
BFS로 그래프 탐색 후 탐색 종료하면 rst 리스트에 push

2.시간복잡도
(4+1)*25^2

3.자료구조
mapSqr = int[][]
chk = bool[][]
rst = int[]
'''


import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
mapSqr = [list(map(int, input().strip())) for _ in range(N)]
chk = list([False] * N for _ in range(N))
rst = []
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]


def bfs(y, x):
    rs = 1
    q = deque()
    q.append((y, x))
    while q:
        (ey, ex) = q.popleft()
        for k in range(4):
            ny = ey + dy[k]
            nx = ex + dx[k]
            if 0 <= nx < N and 0 <= ny < N:
                if chk[ny][nx] == False and mapSqr[ny][nx] == 1:
                    chk[ny][nx] = True
                    q.append((ny, nx))
                    rs += 1
    return rs


totalCnt = 0
for j in range(N):
    for i in range(N):
        if mapSqr[j][i] == 1 and chk[j][i] == False:
            chk[j][i] = True
            totalCnt += 1
            rst.append(bfs(j, i))

rst.sort()
print(totalCnt)
for cnt in rst:
    print(cnt)
