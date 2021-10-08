a = float(input())
b = float(input())
op = input()

result = 0

if b == 0 and (op == "/" or op == "mod" or op == "div"):
    print("Деление на 0!")
    exit()

if op == "+":
    result = a + b
elif op == "-":
    result = a - b
elif op == "*":
    result = a * b
elif op == "/":
    result = a / b
elif op == "mod":
    result = int(a) % int(b)
elif op == "div":
    result = a // b
elif op == "pow":
    result = a ** b

print(result)
