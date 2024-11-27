def func(strings):
    s = []
    for string in strings:
        if len(string) == max(map(len, strings)):
            s.append(string)
    return s

strings = ["short", "longer", "longest", "tiny"]
print(func(strings))