num = int(input("enter a number: "))
steps = 0

while num > 0:
    if num % 2 == 0:
        num = num // 2
    else:
        num = num - 1

    steps += 1

print("Steps",steps)