if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    sort_value = sorted(set(arr))
    print(sort_value[-2])
