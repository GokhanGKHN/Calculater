from art import logo

def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2


operations={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide,
}

def calculater():
    print(logo)
    num1= float(input("What's you the first number: "))
    for operator in operations:
        print(operator)

    should_contiune=True

    while should_contiune:
        operator_symbol=input("Pick an operation : ")
        num2= float(input("What's the next number: "))
        caculation_function = operations[operator_symbol]
        anwser=caculation_function(num1,num2)

        print(f"{num1} {operator_symbol} {num2} = {anwser}")

        if input(f"Type 'y' to continue calculating with {anwser}, or type 'n' to start a new calculater : ")=='y':
            num1=anwser
        else:
            should_contiune=False
            

calculater()


   

    