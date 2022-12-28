for _ in range(int(input())):
    length = int(input())
    nums = list(map(int, input().split()))

    lastNum = nums[0]
    descending = True
    solution = "Yes"
    for i in range(1, length):
        if descending:
            if nums[i] > lastNum:
                descending = False
        else:
            if nums[i] < lastNum:
                solution = "No"
                break

        lastNum = nums[i]
    print(solution)
