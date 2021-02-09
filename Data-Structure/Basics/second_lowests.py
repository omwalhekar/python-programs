
students = []
n = int(input())
for _ in range(n):
    name = input()
    score = float(input())
    students.append([name, score])


def get_score(student):
    return student[1]


scores = list(map(get_score, students))
max_score = min(scores)
students = [students[x] for x in range(n) if(students[x][1] > max_score)]

scores = list(map(get_score, students))
max_score = max(scores)
students = [students[x]
            for x in range(len(students)) if(students[x][1] == max_score)]

print(students)
