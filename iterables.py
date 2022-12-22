from itertools import *
n = input()
a = list(input().split(" "))
t = int(input())
c = 0
for i in combinations(a,t):
    if "a" in i:
        c+=1
print(c/len(list(combinations(a,t))))
