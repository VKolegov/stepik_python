ticket = input()

ticketInt = int(ticket)

firstThreeDigits = ticketInt // 1000
lastThreeDigits = ticketInt % 1000

digit_6 = ticketInt % 10
digit_5 = lastThreeDigits % 100 // 10
digit_4 = lastThreeDigits // 100

digit_3 = firstThreeDigits % 10
digit_2 = firstThreeDigits % 100 // 10
digit_1 = firstThreeDigits // 100

firstThreeDigitsSum = digit_1 + digit_2 + digit_3
lastThreeDigitsSum = digit_4 + digit_5 + digit_6

if firstThreeDigitsSum == lastThreeDigitsSum:
    print("Счастливый")
else:
    print("Обычный")

