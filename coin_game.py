# total_coin10 = [70, 10, 50, 40, 60, 80]
# total_coin9 = [10, 50, 40, 60, 80, 70]
total_coin = list(map(int, input().split()))


def optimalStrategyOfGame(arr, n):
    memo = {}

    def solve(i, j):
        if i > j or i >= n or j < 0:
            return 0

        k = (i, j)
        if k in memo:
            return memo[k]

        option1 = arr[i] + min(solve(i+2, j), solve(i+1, j-1))
        option2 = arr[j] + min(solve(i+1, j-1), solve(i, j-2))

        memo[k] = max(option1, option2)
        return memo[k]

    return solve(0, n-1)


print(optimalStrategyOfGame(total_coin, len(total_coin)))
