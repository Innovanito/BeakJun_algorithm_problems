'''
1. 아이디어
-백트래킹 재귀함수 안에서, for 돌면서 숫자를 선택하고 방문 여부를 확인한다
-재귀 함수에서 M개가 되었을 때 print하고 방문여부를 다시 False로 한다

2.시간복잡도
-8! < 2억

3. 자료구조
-결과값 저장 rst= int[]
-방문여부 확인 chk = bool[]
'''

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

rst = []
chk = [False] * (N+1)


def permute(num):
    if M == num:
        print(' '.join(map(str, rst)))
    for i in range(1, N+1):
        if chk[i] == False:
            chk[i] = True
            rst.append(i)
            permute(num+1)
            chk[i] = False
            rst.pop()


permute(0)
