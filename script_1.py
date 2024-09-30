# A script to sort three numbers in ascending order
try:
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    c = float(input("Enter the third number: "))
    if a>b:
        a, b = b, a
    if b>c:
        b, c = c, b
    if a>b:
        a,b = b, a
    print('Here are your sorted numbers:', a,b,c)
except ValueError as e:
    print(f'Something wrong with your input: {e}')