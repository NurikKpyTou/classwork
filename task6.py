def func(s):
    asd = ""
    for i in s:
        if i.lower() in "ayeiou":
            asd += "g"
        else:
            asd += i
    return asd

print(func(input()))