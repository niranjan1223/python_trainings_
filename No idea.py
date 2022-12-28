n, m = input().split()
arr = list(input().split())
setA = set(input().split())
setB = set(input().split())

arrA = [ i for i in arr if i in setA]
arrB = [ i for i in arr if i in setB]

print(len(arrA) - len(arrB))
