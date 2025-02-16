#calculator project

symbols= ["+", "-", "*", "/", "% mod", "x^y"]
print("Select an operation symbol ")
for i in symbols:
    print(i)
def calc():

    #Determine the oppereation to be executed
    num1 = float(input("first number: "))
    operation= input("Please enter a symbol here ")
    num2 = float(input("second number: "))

    #provides the final answer
    
    if operation == "+":
        print(f"{num1} + {num2} = {num1 + num2} ")
    elif operation== "-":
        print(f"{num1} - {num2} = {num1 - num2} ")
    elif operation== "*":
        print(f"{num1} * {num2} = {num1 * num2} ")
    elif operation== "/":
        print(f"{num1} / {num2} = {num1 / num2} ")
    elif operation== "%":
        print(f"{num1} % {num2} = {num1 % num2} ")  
    elif operation== "^":
        print(f"{num1} ^ {num2} = {num1 ** num2} ")
    else:
        print(f"{operation} is not a valid operation!")

    
calc()
    #To try again

while True:

        tryagain=input("continue Enter(yes), x(no) ")
        
        if tryagain=="x":
            print("goodbye!")
            break
        calc()
