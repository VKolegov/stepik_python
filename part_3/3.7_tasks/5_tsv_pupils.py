classesData = []

for i in range(11):
    classesData += [{"pupils": 0, "totalHeight": 0}]

with open('5_input.tsv', 'r') as inp_file:
    for line in inp_file:
        pupilData = line.strip().split()
        classN = int(pupilData[0])
        height = int(pupilData[2])

        classesData[classN - 1]["pupils"] += 1
        classesData[classN - 1]["totalHeight"] += height


for i in range(11):
    classData = classesData[i]
    if classData["pupils"] == 0:
        print(i + 1, "-")
    else:
        avgHeight = classData["totalHeight"] / classData["pupils"]
        print(i + 1, avgHeight)
