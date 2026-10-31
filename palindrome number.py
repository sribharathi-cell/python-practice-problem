x = int(input("enter a number"))

if x < 0:
    print("False")
else:
    Original= x
    rev = 0

    while x > 0:
        digit = x % 10
        rev = rev * 10 + digit
        x = x // 10

    print(Original == rev)