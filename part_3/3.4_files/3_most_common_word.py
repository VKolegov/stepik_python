output = ""

words = []
word_count = {}

mcw = ""
mcw_count = 0

with open('3_input.txt', 'r') as input_file:
    for line in input_file:
        words += line.strip().lower().split()

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

for word, count in word_count.items():
    if count > mcw_count:
        mcw = word
        mcw_count = count
    elif count == mcw_count:
        if word < mcw:
            mcw = word


with open('3_output.txt', 'w') as output_file:
    output_file.write(mcw + ' ' + str(mcw_count))
