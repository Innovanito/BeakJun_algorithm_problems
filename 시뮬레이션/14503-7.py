# 1.아이디어
# for 과 switch를 사용해 청소가능한 칸과 청소 불가능한 칸을 이동한다
# 청소하면 2로 바꾸고, 동작 불가시 break로 while문 나온다음
# rst를 print한다.

# 2.시간복잡도
# 50^2

# 3.자료구조
# N,M = int
# map1 = int[][]
# r,c,d = int
# rst = int

# 이 코드는 정상 동작하지 않는다 while 문에서 infinite loop가 실행되어요
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
r, c, d = map(int, input().split())
map1 = [list(map(int, input().split())) for _ in range(N)]
rst = 0

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

print('N,M: ', N, M)
print('r,c,d:', r, c, d)
print('map1:', map1)

while 1:
    if map1[r][c] == 1:
        rst += 1
        map1[r][c] = 2

        print('r and c ', r, c)

    switch = True
    for i in range(1, 5):
        ny = r + dy[d-i]
        nx = c + dx[d-i]

        if 0 <= ny < N and 0 <= nx < M:
            if map1[ny][nx] == 0:
                r = ny
                c = nx
                d = (d - i+4) % 4
                print('new r,c ', r, c)
                switch = False
                break

    if switch == True:
        ny = r - dy[d]
        nx = c - dx[d]

        if 0 <= ny < N and 0 <= nx < M:
            if map1[ny][nx] == 1:
                break

            else:
                r = ny
                c = nx

print(rst)
