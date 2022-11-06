def coin_change(change):
    coin = [500, 100, 50, 10, 5, 1]
    cnt = 0
    lst_change = []
    for i in coin:
        cnt = change // i  # 동전 수
        lst_change += [i] * cnt
        change = change % i  # 남은 돈
    return lst_change


# find the possible combinations of coins
coin = [500, 100, 50, 10, 5, 1]
change = 1000
lst_change = []
for i in coin:
    cnt = change // i  # 동전 수
    lst_change += [i] * cnt
    change = change % i  # 남은 돈
print(lst_change)

# destribute the coins


def permute(self, nums):
    rslt = []

    def dfs(temp, elements):
        # gather rslt
        if len(elements) == 0:
            rslt.append(temp[:])  # still remember to use temp[:]
        for e in elements:
            temp.append(e)
            # backtrack
            next_elements = elements[:]
            next_elements.remove(e)
            elements.pop()
            dfs(temp, next_elements)
            temp.pop()

        dfs([], nums)  # first is the current result
        return rslt


print(permute([1, 2, 3]))
