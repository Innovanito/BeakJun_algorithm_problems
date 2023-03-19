'''
1.아이디어
dfs를 이용해서 bfs에서 풀었던 방법에서 
queue 이용 대신에 stack을 이용해 풀어보자

2.시간복잡도
O(V+E)

3.자료구조
pic = int[][]
visit = bool[][]

cnt = int
maxv =int
'''

from collections import deque

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(n)]
chk = [[False] * m for _ in range(n)]

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]


def dfs(y, x):
    rs = 1
    stack = deque()
    stack.append((y, x))
    while stack:
        ey, ex = stack.pop()
        for k in range(4):
            ny = ey + dy[k]
            nx = ex + dx[k]
            if 0 <= ny < n and 0 <= nx < m:
                if map[ny][nx] == 1 and chk[ny][nx] == False:
                    rs += 1
                    chk[ny][nx] = True
                    stack.append((ny, nx))
    return rs


cnt = 0
maxv = 0


for j in range(n):
    for i in range(m):
        if map[j][i] == 1 and chk[j][i] == False:
            chk[j][i] = True
            cnt += 1
            maxv = max(maxv, dfs(j, i))


print(cnt)
print(maxv)
