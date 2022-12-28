if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    score = []
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    for i in student_marks[query_name]:
        score.append(i)

    print(f'{(score[0] + score[1] + score[2]) / 3:.2f}')
