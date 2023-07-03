def subTotal(n, s, lst):
    left = 0
    right = 0
    sub = 0
    minLen = float('inf')

    while left < n:
        if sub < s and right < n:
            sub += lst[right]
            right += 1

        else:
            if sub >= s:
                minLen = min(minLen, right-left)
            sub -= lst[left]
            left += 1

    if minLen == float('inf'):
        return 0

    else:
        return minLen


n, s = map(int, input().split())
lst = list(map(int, input().split()))

rst = subTotal(n, s, lst)
print(rst)
