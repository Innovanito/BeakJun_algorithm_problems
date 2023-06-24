'''
1.아이디어
백트레킹을 써서 제귀함수와 for문으로 해결

2.시간복잡도
8! < 2억

3.자료구조
N,M = int
chk = bool[]
rst = []

'''

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
chk = [False] * (N+1)

rst = []


def recur(num):
    if num == M:
        print(' '.join(map(str, rst)))
        return
    for i in range(1, N+1):
        if chk[i] == False:
            chk[i] = True
            rst.append(i)
            recur(num + 1)
            rst.pop()
            chk[i] = False


recur(0)
