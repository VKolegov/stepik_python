output = ""
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
with open('2_input.txt', 'r') as input_file:
    line = input_file.readline().strip()

    length = len(line)

    i = 0
    while i < length:
        char = line[i]

        n_str = ""
        for j in range(i + 1, length):
            if line[j] in digits:
                n_str += line[j]
            else:
                i = j
                break

        n = int(n_str)

        output += char * n
        if j + 1 == length:
            break

with open('2_output.txt', 'w') as output_file:
    output_file.write(output)
