min_hours = int(input())
max_hours = int(input())
sleep_hours = int(input())

if sleep_hours < min_hours:
    print("Недосып")
elif sleep_hours > max_hours:
    print("Пересып")
else:
    print("Это нормально")

year = int(input())

if (year % 4 == 0) and (year % 100 != 0) or year % 400 == 0:
    print("Високосный")
else:
    print("Обычный")
