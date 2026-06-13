def add(x,y):
    add = x+y
    return add

def subtract(x,y):
    subtract = x-y
    return subtract

def Multiply(x,y):
    Multiply = x*y
    return Multiply

def Divide(x,y):
    if y==0:
        return "Error! Divide by zero is not allowed"
    Divide = x/y
    return Divide

while True:

    operation = input("Enter Operation(+,-,*,/) or E to Exit : ")
    if operation.upper() == "E":
        print("Bye")
        break

    try:
        num_1 = float(input("Enter Fist number : "))
        num_2 = float(input("Enter Second number : "))
        
        match operation:
            case '+':
                print(f"{num_1} + {num_2} = {add(num_1,num_2)}")
            case '-':
                print(f"{num_1} - {num_2} = {subtract(num_1,num_2)}")
            case '*':
                print(f"{num_1} x {num_2} = {Multiply(num_1,num_2)}")
            case '/':
                print(f"{num_1} / {num_2} = {Divide(num_1,num_2)}")
            case _:
                print("Invalid Operation")

    except ValueError:
        print("Invalid Input! Please enter valid input")

    
    