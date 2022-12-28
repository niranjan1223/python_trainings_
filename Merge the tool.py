def merge_the_tools(string, k):
    if k == 1:
        for n in range(len(string)):
            print(string[n])
    else:
        for n in range(k):
            print("".join(sorted(set(string[:k]), key=string.index)))
            string = string[k:]


