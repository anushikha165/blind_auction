def calculator():
    num1 = float(input("enter the 1st number: "))
    should_continue = True
    while should_continue:
        operator = input("chose the operator from (+, - , * , / ) :")
        num2 = float(input("enter the 2nd number: "))
        if operator == "+":
            answer = num1 + num2
        elif operator == "-":
            answer = num1 - num2
        elif operator == "*":
            answer = num1 * num2
        elif operator == "/":
            answer = num1 / num2
        else:
            print("invalid operator")
            continue
        print(f"{num1}{operator}{num2} = {answer}")
        cal = input("type 'y' for continue or 'n' for new calculation: ").lower()
        if cal == "y":
            num1 = answer
        else:
            should_continue = False
calculator()

