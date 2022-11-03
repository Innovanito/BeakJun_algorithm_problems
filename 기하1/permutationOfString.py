def reArrange(str, str2):
    data = permutation(list(str))
    for i in range(len(data)):
        stringData = ''.join(data[i])
        print(stringData)


def permutation(lst):

    if len(lst) == 0:
        return []

    if len(lst) == 1:
        return [lst]

    l = []

    for i in range(len(lst)):
        m = lst[i]

        remLst = lst[:i] + lst[i+1:]
        print('permutation(remLst)', permutation(remLst))

        for p in permutation(remLst):
            l.append([m] + p)

    return l


text = input("단어 입력>> ")
reArrange(text, "")
