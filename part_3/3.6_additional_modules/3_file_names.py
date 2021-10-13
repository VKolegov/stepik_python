import requests

baseUrl = "https://stepic.org/media/attachments/course67/3.6.3/"

filename = input().strip()


def save_text(text):
    with open('3_output.txt', 'w') as output_file:
        output_file.write(text)

#  first file
file = requests.get(filename)
filename = file.text.strip()
print(file.text)

while True:
    print("Downloading: " + baseUrl + filename)
    file = requests.get(baseUrl + filename)
    fileText = file.text.strip()

    firstWord = fileText.split(" ", 2)[0]

    if firstWord.lower() == "we":
        save_text(fileText)
        break
    else:
        filename = fileText
