"""
1.아이디어
-while문으로, 특정조건 종료될때까지 반복
-4방향을 for문을 탐색
- 더이상 탐색 불가능할 경우 뒤로 한칸 후진
-후진 못하면 종료

2.시간복잡도
-O(NM) : 50^2

3.자료구조
-mal: int[][]
-로봇 청소기 위치, 방향, 전체 청소한 곳의 수

추가로 로봇청소기가 청소한 새로운 map을 출력하라

"""

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
        # print('d-i', d-i)
        ny = y + dy[d-i]
        nx = x + dy[d-i]

        if 0 <= ny < N and 0 <= nx < M:
            # 반시계 방향으로 $90^\circ$ 회전한다. 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진한다.
            if map[ny][ny] == 0:
                d = (d-i+4) % 4
                y = ny
                x = nx
                sw = True
                break

    # 4방향 모두 못갈경우 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
    if sw == False:
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


print('final result value cnt is:', cnt)
