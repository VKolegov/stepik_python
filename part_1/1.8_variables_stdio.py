hours = int(input())
minutes = int(input())

minutes += hours * 60

print(minutes)


minutes = int(input())

hours = minutes // 60
minutes = minutes % 60

print(hours)
print(minutes)

requiredMinutes = int(input())
startHour = int(input())
startMinutes = int(input())

wakeUpMinutes = startMinutes + requiredMinutes

minutes = wakeUpMinutes % 60
hour = startHour + (wakeUpMinutes // 60)

print(hour)
print(minutes)
