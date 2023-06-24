from collections import deque

n = int(input())
k = int(input())


map1 = [[0] * n for _ in range(n)]
for _ in range(k):
    row, col = map(int, input().split())
    map1[row-1][col-1] = 1


directions = {}
l = int(input())
for _ in range(l):
    x, c = input().split()
    directions[int(x)] = c


def simul():

    time = 0

    # 북,동,남,서 방향
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    y, x = 0, 0
    # 처음 방향 동쪽
    d = 1

    snake = deque([(y, x)])
    while True:
        ny = y + dy[d]
        nx = x + dx[d]

        # 만약 새로운 이동좌표가 map1을 벗어나거나 뱀끼리 부딪히면 time값을 return(종료)
        if ny >= n or 0 > ny or nx >= n or 0 > nx or (ny, nx) in snake:
            return time+1

        snake.append((ny, nx))

        if map1[ny][nx] == 1:
            map1[ny][nx] = 0
        else:
            snake.popleft()

        y, x = ny, nx

        if time+1 in directions:
            if directions[time+1] == 'D':
                d = (d+1) % 4
            else:
                d = (d-1) % 4

        time += 1


print(simul())


# 드디어 정답
# x와 y의 위치를 햇갈리지 말자 (동서남북 방향)
