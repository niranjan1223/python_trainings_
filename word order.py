words = {}
for _ in range(int(input())):
    word = input()
    words[word] = words.get(word, 0) + 1

print(len(words))
for v in words.values():
    print(v, end=' ')
