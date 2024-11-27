def func(asd):
    s = set()
    res = []
    for i in asd:
        if i not in s:
            s.add(i)
            res.append(i)
    return res

strings = ["apple", "banana", "apple", "orange", "banana"]
print(func(strings))