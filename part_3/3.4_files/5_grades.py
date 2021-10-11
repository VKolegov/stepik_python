student_grades = {}

s = [0, 0, 0]

avg = [0, 0, 0]

students_count = 0

with open('5_input.txt', 'r') as input_file:
    for line in input_file:
        data = line.strip().lower().split(";")

        surname = data[0]

        grades = [int(i) for i in data[1:]]

        for i in range(0, 3):
            s[i] += grades[i]

        student_avg = sum(grades) / 3

        student_grades[surname] = grades
        student_grades[surname] += [student_avg]
        students_count += 1

for i in range(0, 3):
    avg[i] = s[i] / students_count

with open('5_output.txt', 'w') as output_file:
    for grades in student_grades.values():
        output_file.write(str(grades[3]) + '\n')  # student avg
    for a in avg:
        output_file.write(str(a) + ' ')  # overall avg
