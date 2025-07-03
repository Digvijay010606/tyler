import os

def calculator():
    again = "yes"
    while again == "yes":

        os.system('clear')
    
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter a number: "))
    
        operator = input("Enter operator(+ , -, *, /) : ")
        if operator == '+':
            result = num1 + num2
            print(result)
        elif operator == '-':
            result = num1 - num2
            print(result)
        elif operator == '*':
            result = num1 * num2
            print(result)
        elif operator == '/':
            result = num1 / num2
            print(result)
        else:
            print("Enter correct operator")

        print("press Enter to continue or clear to clear: ")
        next_step = input().lower()
        while next_step == "enter":

            if next_step == 'enter':
                print(result)
                num3 = float(input("Enter a number: "))

                operator = input("Enter operator(+ , -, *, /) : ")
                if operator == '+':
                    next_result = result + num3
                    print(next_result)
                elif operator == '-':
                    next_result = result - num3
                    print(next_result)
                elif operator == '*':
                    next_result = result * num3
                    print(next_result)
                elif operator == '/':
                    next_result = result / num3
                    print(next_result)
                else:
                    print("Enter correct operator")

                print("press Enter to continue or clear to clear: ")
                next_step = input().lower()
    
        again = input("Enter (yes/no): ").lower()
        
        
        
calculator()