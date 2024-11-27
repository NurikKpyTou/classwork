def func(strings):
    res = []
    for i in strings:
        if len(i) % 2 == 0:
            res.append(i[::-1])
        else:
            res.append(i)
    return res

strings = ["Hello", "world", "Python", "is", "great"]
print(func(strings))
