# Multiplication calculator useing function

def multiplication(num):
    for i in range(10):
        print(num, "X", i+1, "=", num*(i+1))
number = float(input("Enter a number: "))
multiplication(number)