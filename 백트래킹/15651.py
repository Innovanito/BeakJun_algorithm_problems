'''
1.아이디어
n^m의 경우의 수를 가지는 수열
n == m일 때 종료
2.시간복잡도
7^7= 80만

3.자료구조
n,m = int
rst = []
chk = bool[n][m]
'''

import sys
input = sys.stdin.readline


def dfs(n, lst):
    if n == M:
        rst.append(lst)
        return

    for j in range(1, N+1):
        dfs(n+1, lst+[j])


N, M = map(int, input().split())
rst = []
dfs(0, [])
for lst in rst:
    print(*lst)
