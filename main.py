import logo



#Add function
def add(n1, n2):
    return n1 + n2

#Substract
def substract(n1,n2):
    return n1 - n2

#Multiply
def multiply(n1,n2):
    return n1 * n2

#Divide
def divide(n1,n2):
    return n1 / n2

#dictionary
operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide
}
    

def calculator():
    print(logo.logo)

    n1 = float(input("What's the first number? "))

    for symbols in operations:
        print(symbols)

    should_continue = True

    while should_continue:
        operator_selected = str(input("Pick an operator: "))
        n2 = float(input("What's the next number? "))
        calculate = operations[operator_selected]
        answer = calculate(n1,n2)

        print(f"{n1} {operator_selected} {n2} = {answer}")

        if input(f" Type 'y' to continue calcultaing with {answer} and n to perform a new calculation  ") == "y":
            n1 = answer
        else:
            should_continue = False
            calculator()



calculator()










