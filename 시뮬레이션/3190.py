# 1.아이디어
# while을 사용해서 map1을 그리고 snake의 값을 매 초마다 갱신을 해서
# 자기 몸과 부딪히거나 벽에 닿으면 break

# 2.시간복잡도
# 100^2 < 2억

# 3.자료구조
# N = int
# K = int
# appleLoc = int[][]
# L =int
# snakeDir = [int][string]
# snake = int[][]
# map1? = int[][]
# cnt = int


import sys
input = sys.stdin.readline

N = int(input())
K = int(input())
appleLoc = [list(map(int, input().split())) for _ in range(K)]
L = int(input())
TimeandDir = [list(map(str, input().split())) for _ in range(L)]
print(N, K, appleLoc, L, TimeandDir)

snake = [[1, 1]]
# TimeandDir의 첫번째 값 쓸 때 항상 int로 바꿔서 쓰기!!

# 동남서북 순서
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

# 처음 방향 동쪽
d = 0

# 뱀의 처음 좌표
y = 1
x = 1

# 뱀이 충돌한다 변수
switch = True

# 뱀의 이동 업데이트
# i는 i초이다.
for i in range(1, N ^ 2):

    # 머리가 이동했을 때 사과가 있을 경우
    hy, hx = snake.pop()
    snake.append([hy, hx])

    for apple in appleLoc:
        ay, ax = apple.pop()
        if hy == ay and hx == ax:
            snake.append

    # 사과가 없을 경우

    for lst in snake:
        ey, ex = lst.pop()
        X, C = TimeandDir.pop()
        X = int(X)
        # 시간이 i초 일 때 뱀의 움직임
        if X == i:
            # 뱀 변환 정보 C== L일때
            if C == 'L':
                nd = (d-1) % 4
                ny = y + dy[nd]
                nx = x + dx[nd]

            # 뱀 변환 정보 C== R일때
            elif C == 'R':
                nd = (d+1) % 4
                ny = y + dy[nd]
                nx = x + dx[nd]

        # 시간이 i초가 아닐때 뱀의 움직임
        else:
            TimeandDir.append([X, C])
            ny = ey + dy[d]
            nx = ex + dx[d]

        # 범위 안에 있을 때
        if 1 <= ny <= N and 1 <= nx <= N:
            # 뱀의 몸이 충돌하지 않을 떄
            for each in snake:
                eachY, eachX = each.pop()
                if eachY == ny and eachX == nx:
                    switch = False
                    cnt = i
                    break

            if switch:
                snake.append([ny, nx])

            else:
                cnt = i
                break

# 사과를 먹었을 때의 경우 추가해주기

print(i)


'''
이 알고리즘을 실패했다

왜냐하면 문제 상황을 재대로 정의하지 않고
코딩을 추가하는 식으로 했기 때문이다

뱀이 움직일 때
사과를 먹을 때
자기 스스로 부딪히거나 벽에 닿을 때 구체적으로 상황을 정하고 코딩을 하자
'''
