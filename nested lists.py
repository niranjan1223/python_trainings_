if __name__ == '__main__':
    score_list = {}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        if score in score_list:
            score_list[score].append(name)
        else:
            score_list[score] = [name]

    final_list = [(key, value) for key, value in score_list.items()]
    final_list.sort()
    output = final_list[1][1]
    output.sort()
    for i in output:
        print(i)
