# This is a simple text based calculator made by Andrew Hess for a school project
import random


def menu():
    """
    
    Menu function which takes user input and decides
    which function to call
    """
    menu_loop = True
    while menu_loop:
        menu_loop = False
        try:
            inpt = input(
                "Would you like to add, subtract, multiply, divide, power, root, or random: ")
        except:
            print("I did not understand your response please try again")
            menu_loop = True
        inpt = inpt.lower()
        if inpt[0] == 'a':
            return 1
        elif inpt[0] == 's':
            return 2
        elif inpt[0] == 'm':
            return 3
        elif inpt[0] == 'd':
            return 4
        elif inpt[0] == 'p':
            return 5
        elif inpt == 'r':
            print("Please specify root or random")
        elif inpt[0] == 'r' and inpt[1] == 'o' or inpt == 'root':
            return 6
        elif inpt[0] == 'r' and inpt[1] == 'a' or inpt == 'random':
            return 7
        else:
            print("I did not understand your response please try again")
            menu_loop = True


def function_close():
    """
    
    Used to either contine using program with another
    function or close the program
    """
    try_loop = True
    while try_loop:
        try:
            cont = str(input("Do you want to use another function?: "))
            try_loop = False
        except:
            print("I did not understand your response please try again",
                  sep='', end='\n')
        cont = cont.lower()
        if cont[0] == "n":
            exit()
        elif cont[0] != 'y':
            print("I did not understand your response please try again",
                  sep='', end='\n')
            try_loop = True
        else:
            return False


def add():
    """
    
    Function for adding
    """
    i = -1
    loop_var = True
    while loop_var:  # used so user can continuously input numbers
        num = str(
            input("Type a number you would like to add. Type done when finished: "))
        num = num.lower()
        if num[0] == 'd':  # used if user if finished with a function
            loop_var = function_close()
        else:
            try:
                num = float(num)
                i += 1
            except:
                print("I did not understand your response please try again",
                      sep='', end='\n')
                i = -1
            if i == 0:#Used to determine wether user has already input
                total = num
                i += 1
            elif i != -1 and i > 0:
                total += num
                i = -1
                print(f"{total}" + "\n")


def subtract():
    """
    
    Function for subtracting
    """
    i = -1
    loop_var = True
    while loop_var:  # used so user can continuously input numbers
        num = str(
            input("Type a number you would like to subtract. Type done when finished: "))
        num = num.lower()
        if num[0] == 'd':  # used if user if finished with a function
            loop_var = function_close()
        else:
            try:
                num = float(num)
                i += 1
            except:
                print("I did not understand your response please try again",
                      sep='', end='\n')
                i = -1
            if i == 0:
                total = num
                i += 1
            elif i != -1 and i > 0:
                total = total - num
                i = -1
                print(f"{total}" + "\n")


def multiply():
    """
    
    Function for multiplying
    """
    i = -1
    loop_var = True
    while loop_var:  # used so user can continuously input numbers
        num = str(
            input("Type a number you would like to multiply. Type done when finished: "))
        num = num.lower()
        if num[0] == 'd':  # used if user is finished with a function
            loop_var = function_close()
        else:
            try:
                num = float(num)
                i += 1
            except:
                print("I did not understand your response please try again",
                      sep='', end='\n')
                i = -1
            if i == 0:
                total = num
                i += 1
            elif i != -1:
                total = total * num
                i = -1
                print(f"{total}" + "\n")


def divide():
    """
    
    Function for dividing
    """
    i = -1
    loop_var = True
    while loop_var:  # used so user can continously input numbers
        num = str(
            input("Type a number you would like to divide. Type done when finished: "))
        num = num.lower()
        if num[0] == 'd':  # used if user if finished with a function
            loop_var = function_close()
        else:
            try:
                num = float(num)
                i += 1
            except:
                print("I did not understand your response please try again",
                      sep='', end='\n')
                i = -1
            if i == 0:
                total = num
                i += 1
            elif i != -1:
                if num!= 0:
                    mod = total % num
                    floor = total // num
                    total = total / num
                    i = -1
                    print(
                        f"{total}, floor division = {floor}, modulus = {mod}", sep='', end='\n')
                elif num == 0:
                    print("Cannot divide by zero please try again")

def power():
    """
    
    Function for finding exponents
    """
    i = -1
    loop_var = True
    while loop_var:  # used so user can continously input numbers
        num = str(
            input("Type a number to raise to a power. Type done when finished: "))
        num = num.lower()
        if num[0] == 'd':  # used if user if finished with a function
            loop_var = function_close()
        else:
            try:
                num = float(num)
                i += 1
            except:
                print("I did not understand your response please try again",
                      sep='', end='\n')
                i = -1
            if i == 0:
                total = num
                i += 1
            elif i != -1:
                total = total ** num
                i = -1
                print(f"{total}" + "\n")


def root():
    """
    
    Function for finding any root(works with negatives)
    """
    i = -1
    loop_var = True
    while loop_var:  # used so user can continously input numbers
        num = str(input("Type a number to find a root. Type done when finished: "))
        num = num.lower()
        if num[0] == 'd':  # used if user if finished with a function
            loop_var = function_close()
        else:
            try:
                num = float(num)
                i += 1
            except:
                print("I did not understand your response please try again",
                      sep='', end='\n')
                i = -1
            if i == 0:
                total = num
                i += 1
            elif i != -1:
                total = total ** (1/num)
                i = -1
                print(f"{total}" + "\n")


def rand():
    """
    
    Generates a random number in a user defined range
    """
    loop_var = True
    while loop_var:
        num = input(
            "Type the amount of numbers you want. Type done when finished: ")
        num = num.lower()
        if num[0] == 'd':  # used if user if finished with a function
            loop_var = function_close()
        else:
            try_loop = True
            while try_loop:
                try:
                    num = int(num)
                except:
                    print(
                        "I did not understand your response please try again", sep='', end='\n')
                print("Enter the range of numbers(lowest than highest): ")
                try:
                    low = int(input())
                    high = int(input())
                    try_loop = False
                except:
                    print(
                        "I did not understand your response please try again", sep='', end='\n')
            for x in range(num):
                print(random.randrange(low, high))


def main():
    """
    
    Main function used to call menu
    """
    loop = True
    while loop:
        choice = menu()
        if choice == 1:
            add()
        elif choice == 2:
            subtract()
        elif choice == 3:
            multiply()
        elif choice == 4:
            divide()
        elif choice == 5:
            power()
        elif choice == 6:
            root()
        elif choice == 7:
            rand()

if __name__ == "__main__":
    main()
