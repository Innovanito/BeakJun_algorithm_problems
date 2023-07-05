# 1.아이디어
# 선형 탐색 이용하면 시간복잡도가 N*M이 10^10이므로
# 이진탐색 이용
# 2.시간복잡도
# O(NlgN + MlgN) = 3* 10^5
# 3.자료구조
# n ,m= int
# lstN, lstM = int[]


n = int(input())
lstN = list(map(int, input().split()))
m = int(input())
lstM = list(map(int, input().split()))

lstN.sort()


def logSearch(start, end, target):
    if start == end:
        if lstN[start] == target:
            print(1)
        else:
            print(0)
        return

    mid = (start+end)//2

    if lstN[mid] >= target:
        logSearch(start, mid, target)
    else:
        logSearch(mid+1, end, target)


for each in lstM:
    logSearch(0, n-1, each)
