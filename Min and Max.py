N, M = map(int, input().split())

l = []
for n in range(N):
    one, two = map(int, input().split())
    l.append(min(one, two))

print(max(l))
