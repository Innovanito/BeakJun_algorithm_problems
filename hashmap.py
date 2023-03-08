nums = [4, 1, 7, 9, 3, 16, 5]

target = 14

seen = {}

for v in nums:
    print("value in", v)
    complement = target - v

    if complement in seen:
        print(f"complement number found {complement} and {v}")

    else:
        seen[v] = complement
