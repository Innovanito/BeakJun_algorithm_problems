'''
1.아이디어
nPm 문제로 제귀함수와 for문으로 푼다
중복 없이 => 방문여부 확인 => chk[] 사용
제귀함수 종료 조건 num == M일 때
2.시간복잡도
8!

3.자료구조
N,M = int
chk = bool[]

'''

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
chk = [False] * (N+1)
rst = []
lst = []


def recur(num, lst):
    if num == M:
        rst.append(lst)
        return

    for j in range(1, N+1):
        if chk[j] == False:
            chk[j] = True
            recur(j+1, lst + [j])
            chk[j] = False


recur(0, lst)

for singleLst in rst:
    print(*singleLst)
