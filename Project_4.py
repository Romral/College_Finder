
def add(a,b):
    addition = a + b
    print(f"The sum of {a} and {b} is {addition}") #formatted strings

def subtract(a,b):
    subtraction = a - b
    print(f"The result of subtracting {b} from {a} is {subtraction}")

def multiply(a,b):
    multiplication = a * b
    print(f"The multiplication of {a} and {b} is {multiplication}")

def division(a,b):
    division = a / b
    print(f"The sum of {a} and {b} is {division}")

def modulus(a,b):
    mod = a % b
    print(f"The sum of {a} and {b} is {mod}")

option = 'y'
while option == 'y':
    number1,operator,number2 = map(str, input("Enter your equation: ").split())
    number1 = int(number1)
    number2 = int(number2)

    if operator == '+':
        add(number1,number2)
        
    elif operator == '-':
        subtract(number1,number2)
        
    elif operator == '*':
        multiply(number1,number2)
        
    elif operator == '/':
        division(number1,number2)

    elif operator == '%':
        modulus(number1,number2)
        
    else:
        print("Invalid Typo Error! Type something like - 4 + 3")

    option = input("Would you like to enter another equation? (y/n)\n")
    