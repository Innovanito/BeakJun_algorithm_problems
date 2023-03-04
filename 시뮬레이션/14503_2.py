
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
    # print("d",d)
    for i in range(1, 5):
        # print("d-i", d-i)
        ny = y + dy[d-i]
        nx = x + dx[d-i]
        if 0 <= ny < N and 0 <= nx < M:
            if map[ny][nx] == 0:
                d = (d-i+4) % 4
                y = ny
                x = nx
                sw = True
                break

    # 4방향 모두 있지 않은경우
    if sw == False:
        # 뒤쪽 방향이 막혀있는 지확인
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
