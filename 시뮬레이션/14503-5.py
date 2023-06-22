# 1.아이디어
# 문제의 조건대로 알고리즘 구조를 짜면 된다.
# 문제가 구체적으로 구조를 주었으니 이 구조 그대로 알고리즘 짜기
# 청소한 방을 map1에서 2로 바꿀것임

# 2.시간복잡도
# N*M = 50^2 < 2억

# 3.자료구조
# N,M : int
# rst : int
# map1 : int[][]

# =-> 실패
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
r, c, d = map(int, input().split())
map1 = [list(map(int, input().split())) for _ in range(N)]
rst = 0
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


while 1:
    if map1[r][c] == 0:
        map1[r][c] = 2
        rst += 1
        print('new r and c ', r, c)
    switch = True
    for i in range(1, 5):
        y = r + dy[d-i]
        x = c + dx[d-i]
        print('y and x', y, x)
        if 0 <= y < N and 0 <= x < M:
            if map1[y][x] == 0:
                r = y
                c = x
                d = (d-i) % 4
                print('r and c value renewed', r, c)
                switch = False
                break

    if (switch):
        y = r - dy[d]
        x = c - dy[d]
        if 0 <= y < N and 0 <= x < M:
            if map1[y][x] != 1:
                r = y
                c = x
                print('r and c value renewed', r, c)
            else:
                break


print(rst)
for lst in map1:
    print(*lst)
