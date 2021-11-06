print("Ban muon ghi de hay them noi dung vao file?")
mode= input("> ") + "+"

contents = []
print("Nhap noi dung cho file")
while True:
    line = input("> ")
    if len(line) ==0:
        break
    contents.append(line + '\n')

with open('demo.txt', mode, encoding='utf8') as file:
    file.writelines(contents)
with open('demo.txt') as file:
    print(file.read())