import numpy
n, m = input().split()
lis = []
for i in range(int(n)):
    lis.append(list(map(int, input().split())))
my_array = numpy.array(lis)
print(numpy.mean(my_array, axis = 1))
print(numpy.var(my_array,axis = 0))
print(round((numpy.std(my_array)), 11))
