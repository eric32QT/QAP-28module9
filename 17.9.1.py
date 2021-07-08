c = int(input('The length of list:'))
x =[]
for i in range(c+1):
    n = int(input('Jour number:'))
    if c > 99 or c <= 0:
        raise ValueError(f"You entered the {c}. Please input numbers from 1 til 99.")
    x.append(i)

a = int(input('Input some number:'))

x.append(a)

for i in range(len(x)):
    for j in range(len(x) - i - 1):
        if x[j] > x[j + 1]:
            x[j], x[j + 1] = x[j + 1], x[j]
print(x)


def binary_search(array, key):
    low_bount = 0
    upp_bount = len(array) - 1

    while low_bount <= upp_bount:
        center = (low_bount + upp_bount) // 2

        if array[center] == key:
            return center

        elif array[center] > key:
            upp_bount = center - 1

        elif array[center] < key:
            low_bount = center + 1

    return None


print(binary_search(x, c))