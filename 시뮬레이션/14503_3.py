'''
1. 아이디어
-while문 특정조건 종료될때까지 반복
-4방향을 for문으로 탐색
-더이상 탐색 불가능 - 뒤로 한 칸 후진
-후진 불가능 시 종료

2. 시간복잡도
-O(NM): 50^2

3.자료구조
map: int[][]
로봇청소기 위치, 방향, 전체 청소한 곳 수
'''

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
y, x, d = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(N)]
cnt = 0

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

while 1:
    if map[y][x] == 0:
        map[y][x] = 2
        cnt += 1
    sw = False
    for i in range(1, 5):
        ny = y + dy[d-i]
        nx = x + dx[d-i]
        if 0 <= ny < N and 0 <= nx < M:
            if map[ny][nx] == 0:
                # 그 방향 회전 후 다음 칸 전진
                d = (d - i+4) % 4
                y = ny
                x = nx
                sw = True
                break

    if sw == False:
        # 뒤쪽 방향이 막혀있는 지 확인
        ny = y - dy[d]
        nx = x - dx[d]
        if 0 <= ny < N and 0 <= nx < M:
            if map[ny][nx] == 1:
                break
            else:
                y = ny
                x = nx

        else:
            break


print(cnt)
