t = int(input())
c = 'H'

# top cone
q = t * 2
for i in range(q):
    if i % 2 != 0:
        print((c * i).center(q))

# top second part

for i in range(t + 1):
    print((c * t).center(q) + (' ').center(q) + (c * t).center(q))

# middle space
b = (t * 5)
for i in range(int((t + 1) / 2)):
    print((c * b).center(b + (t - 1)))

# second bottom part

for i in range(t + 1):
    print((c * t).center(q) + (' ').center(q) + (c * t).center(q))

# bottom cone
for i in reversed(range(q)):
    if i % 2 != 0:
        print(('').rjust(q + q) + (c * i).center(q))
