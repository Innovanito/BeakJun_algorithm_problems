# 1.아이디어
# N과 M을 입력 받고 현재 위치와 방향을 입력 받은 후
# 지도값 받은 후
# 제귀함수 조건에 맞춰 청소 후 값을 2로 바꾸고 rst +=1
# rst를 print해준다

# 2.시간복잡도
# N*M = 50^2 < 2억

# 3.자료구조
# N,M = int
# r,c,d = int
# map1 = int[][]
# rst = int


import sys
input = sys.stdin.readline

N, M = map(int, input().split())
r, c, d = map(int, input().split())
map1 = [list(map(int, input().split())) for _ in range(N)]
map = [list(map(int, input().split())) for _ in range(N)]
rst = 0
run = True

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]


def robot(y, x, v):
    global run
    while run:
        if map1[y][x] == 0:
            global rst
            rst += 1
            map1[y][x] = 2
            for k in range(4):
                ny = y + dy[(v-k) % 4]
                nx = x + dx[(v-k) % 4]
                print('v and ny and nx', v, ny, nx)
                if (map1[ny][nx] == 0):
                    y = ny
                    x = nx
                    v = v-k
                    print('new y and x', y, x)
                    break
                if k == 3:
                    ny = y + dy[-2]
                    nx = x + dx[-2]

                    if map1[ny][nx] == 1:
                        run = False

                    else:
                        y = ny
                        x = nx

        else:
            return


def robot2(y, x, v):
    global run
    while run:
        if map1[y][x] == 0:
            global rst
            rst += 1
            map1[y][x] = 2
            for k in range(1, 5):
                ny = y + dy[v-k]
                nx = x + dx[v-k]
                # print('v and ny and nx', v, ny, nx)
                if (map1[ny][nx] == 0):
                    y = ny
                    x = nx
                    v = (v-k) % 4
                    print('new y and x', y, x)
                    break
                if k == 3:
                    ny = y - dy[v]
                    nx = x - dx[v]

                    if map1[ny][nx] == 1:
                        print('run finished')
                        run = False

                    else:
                        y = ny
                        x = nx

        else:
            return


def robot3(y, x, v):
    global run
    while run:
        if map1[y][x] == 0:
            global rst
            rst += 1
            map1[y][x] = 2
            for k in range(4):
                ny = y + dy[(v-k) % 4]
                nx = x + dx[(v-k) % 4]
                print('v and ny and nx', v, ny, nx)
                if 0 <= ny < N and 0 <= nx < M:
                    if (map1[ny][nx] == 0):
                        y = ny
                        x = nx
                        v = v-k
                        print('new y and x', y, x)
                        break
                    if k == 3:
                        ny = y + dy[-2]
                        nx = x + dx[-2]
                        if 0 <= ny < N and 0 <= nx < M:
                            if map1[ny][nx] == 1:
                                run = False

                            else:
                                y = ny
                                x = nx

        else:
            return


# robot3(r, c, d)

# print(rst)
# for line in map1:
#     print(*line)

while 1:
    if map[r][c] == 0:
        map[r][c] = 2
        rst += 1
    sw = False
    for i in range(1, 5):
        ny = r + dy[d-i]
        nx = c + dx[d-i]
        if 0 <= ny < N and 0 <= nx < M:
            if map[ny][nx] == 0:
                d = (d-i+4) % 4
                r = ny
                c = nx
                sw = True
                break
    if sw == False:
        ny = r - dy[d]
        nx = c - dx[d]
        if 0 <= ny < N and 0 <= nx < M:
            if map[ny][nx] == 1:
                break
            else:
                r = ny
                c = nx

        else:
            break

print(rst)
