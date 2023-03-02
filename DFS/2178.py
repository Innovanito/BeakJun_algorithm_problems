"""
1. 아이디어
-2중 for, 값 1 and 방문 X => DFS 와 area += 1
-DFS를 통해 찾은 값을 저장 후 정렬 해서 출력

2. 시간복잡도
-DFS: O(V+E)
-V,E: N^2, 4*N^2
-V+E: 5*25^2 < 2억

3.자료구조
-그래프: int[][]
-방문여부: bool[][]
-각각 넓이: int[]
-넓이결과값: int[]
"""

import sys
input = sys.stdin.readline

N = int(input())
map = [list(map(int, input().strip())) for _ in range(N)]
check = [[False] * N for _ in range(N)]

result = []
area = 0

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

print('N', N)
print("map", map)
print('check', check)


def dfs(j, i):
    global area
    area += 1
    for k in range(4):
        ny = j + dy[k]
        nx = i + dx[k]
        if 0 <= ny < N and 0 <= nx < N:
            if check[ny][nx] == False and map[ny][nx] == 1:
                check[ny][nx] = True
                dfs(ny, nx)


for j in range(N):
    for i in range(N):
        if check[j][i] == False and map[j][i] == 1:
            check[j][i] = True
            area = 0
            dfs(j, i)
            result.append(area)

result.sort()
print(len(result))

for i in result:
    print(i)
