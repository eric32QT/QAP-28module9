tickets = int(input('Number of participants:'))
result = 0

for person in range(tickets,):
    age = int(input('Participants age:'))
    if age < 18:
        result += 0
    elif 18 <= age < 25:
        result += 990
    elif age <= 25:
        result += 1390
if tickets > 3:
    result = result - (result * 0.1)
print('Payment sum including discount', result)
