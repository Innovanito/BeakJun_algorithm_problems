'''
1. 아이디어
nCm 문제
백트레킹 문제로 제귀함수와 for문을 이용

2. 시간복잡도
8! < 2억

3.자료구조

n,m = int
방문 확인 chk = bool[]
rst = int[]
'''

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
rst = []


def dfs(n, s, lst):
    if n == M:
        rst.append(lst)
        return

    for j in range(s, N+1):
        dfs(n+1, j+1, lst+[j])


dfs(0, 1, [])
for lst in rst:
    print(*lst)

print(rst)

'''


'''

# N, M = 3, 2 일 때

# dfs(0, 1, [])


# def dfs(n, s, lst) < 0, 1, [] > :
#     if n == M < 0 !=  2 >:
#         rst.append(lst)
#         return

#     for j in range(s, N+1)<1,4> j =1 :
#         dfs(n+1, j+1, lst+[j])<1,2,[1]>

# def dfs(n, s, lst) < 1, 2, [1] > :
#     if n == M < 1 !=  2 >:
#         rst.append(lst)
#         return

#     for j in range(s, N+1)<2,4> j= 2:
#         dfs(n+1, j+1, lst+[j])<2,3,[1,2]>


# def dfs(n, s, lst) < 2, 3, [1, 2] > :
#     if n == M < 2 ==  2 >:
#         rst.append(lst) => rst = [[1,2]]
#         return


# def dfs(n, s, lst) < 1, 2, [1] >:
#     if n == M < 1 !=  2 >:
#         rst.append(lst)
#         return

#     for j in range(s, N+1) < 3, 4 > j = 3:
#         dfs(n+1, j+1, lst+[j]) < 2, 4, [1, 3] >


# def dfs(n, s, lst) < 2, 4, [1, 3] >:
#     if n == M < 2 ==  2 >:
#         rst.append(lst)
#         return


# def dfs(n, s, lst) < 0, 1, [] > :
#     if n == M < 0 !=  2 >:
#         rst.append(lst)
#         return

#     for j in range(s, N+1)<2,4> j = 2:
#         dfs(n+1, j+1, lst+[j])<1,3,[2]>


# def dfs(n, s, lst) < 1, 3, [2] > :
#     if n == M < 1 !=  2 >:
#         rst.append(lst)
#         return

#     for j in range(s, N+1)<3,4> j = 3:
#         dfs(n+1, j+1, lst+[j])<2,4,[2,3]>


# def dfs(n, s, lst) < 2, 4, [2, 3] > :
#     if n == M < 2 ==  2 >:
#         rst.append(lst)
#         return
