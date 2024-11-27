def func(s):
    words = s.lower().split()
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts
def rem(s):
    punc = ".,!?;:'\"()-[]{}<>"
    result = ""
    for char in s:
        if char not in punc:
            result += char
    return result
s = input()
s = rem(s)
print(func(s))