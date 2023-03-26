'''
1.아이디어
그리디 알고리즘으로 전체탐색을 진행
N과 M을 입력으로 받고
recur(num)에서 num == M일때 프린트
start와 num을 같이 인자로 받아서 제귀함수 돌릴 때 같이 넣어준다
2.시간복잡도
N!
N<8 => 가능

3.자료구죠
N,M => int
rst => int[]
방문여부 visit => bool[]
'''

import sys
input = sys.stdin.readline


N, M = map(int, input().split())
rst = []


def recur(start, num):
    if num == M:
        print(' '.join(map(str, rst)))
        return
    for i in range(start, 1+N):
        rst.append(i)
        recur(i+1, num+1)
        rst.pop()


recur(1, 0)
