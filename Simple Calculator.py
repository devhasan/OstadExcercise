"""
Project 1: Simple Calculator by Hasan Mahmud
Full Stack Web Development with Python, Django & React-Batch 2
"""
#1 function definitions:
def addition(num1, num2):
    result = num1 + num2
    print("Addition:", num1, "+", num2, "=", result)
    return result

def subtract(num1, num2):
    result = num1 - num2
    print("Subtract:", num1, "-", num2, "=", result)
    return result

def multiplicaion(num1, num2):
    result = num1 * num2
    print("Multiplicaion:", num1, "*", num2, "=", result)
    return result

def division(num1, num2):
    result = num1 / num2
    print("Division:", num1, "/", num2, "=", result)
    return result

def modulus(num1, num2):
    result = num1 % num2
    print("Modulus:", num1, "%", num2, "=", result)
    return result

#2. Implement User Input Handling:
print("Select Operation:\n 1. Add \n 2. Subtract \n 3. Multiply \n 4. Divide \n 5. Modulus")
try:
    operator= int(input("Enter choice (1/2/3/4/5): "))
    val1 = float(input("Enter first number: "))
    val2 = float(input("Enter second number: "))

    #3. Conditional Logic:
    if operator == 1:
        addition(val1,val2)
    elif operator == 2:
        subtract(val1,val2)
    elif operator == 3:
        multiplicaion(val1,val2)
    elif operator == 4:
        division(val1,val2)
    elif operator == 5:
        modulus(val1,val2)
    else:
        print("Invalid Operator. Try again")
    
except Exception as e:
    print(e)
