
def multiplication(num):
    print(type(num))
    for i in range(10):
        print(num, "X", i+1, "=", num*(i+1))

number = float(input("Enter a number: "))
multiplication(number)