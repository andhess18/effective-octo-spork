#This is a simple text based calculator made by Andrew Hess for a school project
import random
def menu():
    menuLoop = True
    while(menuLoop):
        menuLoop = False
        try:
            inpt = input("Would you like to add, subtract, multiply, divide, power, root, or random: ")
        except:
            print("I did not understand your response please try again")
            menuLoop = True
        inpt=inpt.lower()
        if(inpt[0] == 'a'):
            return 1
        elif(inpt[0] == 's'):
            return 2
        elif(inpt[0] == 'm'):
            return 3
        elif(inpt[0] == 'd'):
            return 4
        elif(inpt[0] == 'p'):
            return 5
        elif(inpt[0] == 'r' and inpt[1] == 'o'):
            return 6
        elif(inpt[0] == 'r' and inpt[1] == 'a'):
            return 7
        else:
            print("I did not understand your response please try again")
            menuLoop = True
def functionClose(): 
    tryLoop = True
    while(tryLoop):
        try:
            cont = str(input("Do you want to use another function?: "))
            tryLoop = False
        except:
            print("I did not understand your response please try again", sep='',end='\n')
        cont = cont.lower()
        if(cont[0]=="n"):
            exit()
        elif(cont[0] != 'y'):
            print("I did not understand your response please try again", sep='',end='\n')
            tryLoop = True  
        else:
            return False
def add():
    i = -1
    loopvar = True
    while(loopvar):#used so user can continously input numbers
        num = str(input("Type a number you would like to add. Type done when finished: "))
        num = num.lower()
        if(num[0]=='d'):#used if user if finished with a function 
            loopvar=functionClose()
        else:
            try:
                num = float(num)
                i+=1
            except:
                print("I did not understand your response please try again", sep='',end='\n') 
                i = -1
            if(i==0):
                total = num
                i += 1
            elif(i != -1 and i > 0):
                total += num
                i=-1
                print(f"{total}" + "\n")
def subtract():
    i = -1
    loopvar = True
    while(loopvar):#used so user can continously input numbers
        num = str(input("Type a number you would like to subtract. Type done when finished: "))
        num = num.lower()
        if(num[0]=='d'):#used if user if finished with a function 
            loopvar=functionClose()
        else:
            try:
                num = float(num)
                i+=1
            except:
                print("I did not understand your response please try again", sep='',end='\n') 
                i = -1
            if(i==0):
                total = num
                i += 1
            elif(i != -1 and i > 0):
                total = total - num
                i=-1
                print(f"{total}" + "\n")
def multiply():
    i = -1
    loopvar = True
    while(loopvar):#used so user can continously input numbers
        num = str(input("Type a number you would like to multiply. Type done when finished: "))
        num = num.lower()
        if(num[0]=='d'):#used if user if finished with a function 
            loopvar=functionClose()
        else:
            try:
                num = float(num)
                i+=1
            except:
                print("I did not understand your response please try again", sep='',end='\n') 
                i = -1
            if(i==0):
                total = num
                i += 1
            elif(i != -1):
                total = total * num
                i=-1
                print(f"{total}" + "\n")
def divide():
    i = -1
    loopvar = True
    while(loopvar):#used so user can continously input numbers
        num = str(input("Type a number you would like to divide. Type done when finished: "))
        num = num.lower()
        if(num[0]=='d'):#used if user if finished with a function 
            loopvar=functionClose()
        else:
            try:
                num = float(num)
                i+=1
            except:
                print("I did not understand your response please try again", sep='',end='\n') 
                i = -1
            if(i==0):
                total = num
                i += 1
            elif(i != -1):
                mod = total % num
                floor = total // num
                total = total / num
                i=-1
                print(f"{total}, floor division = {floor}, modulus = {mod}", sep='',end='\n')
def power():
    i = -1
    loopvar = True
    while(loopvar):#used so user can continously input numbers
        num = str(input("Type a number to raise to a power. Type done when finished: "))
        num = num.lower()
        if(num[0]=='d'):#used if user if finished with a function 
            loopvar=functionClose()
        else:
            try:
                num = float(num)
                i+=1
            except:
                print("I did not understand your response please try again", sep='',end='\n') 
                i = -1
            if(i==0):
                total = num
                i += 1
            elif(i != -1):
                total = total ** num
                i=-1
                print(f"{total}" + "\n")
def root():
    i = -1
    loopvar = True
    while(loopvar):#used so user can continously input numbers
        num = str(input("Type a number to find a root. Type done when finished: "))
        num = num.lower()
        if(num[0]=='d'):#used if user if finished with a function 
            loopvar=functionClose()
        else:
            try:
                num = float(num)
                i+=1
            except:
                print("I did not understand your response please try again", sep='',end='\n') 
                i = -1
            if(i==0):
                total = num
                i += 1
            elif(i != -1):
                total = total ** (1/num)
                i=-1
                print(f"{total}" + "\n")
def rand():
    loopvar = True
    while(loopvar):
        num = input("Type the amount of numbers you want. Type done when finished: ")
        num = num.lower()
        if(num[0]=='d'):#used if user if finished with a function 
            loopvar=functionClose()
        else:
            tryloop = True
            while(tryloop):
                try:
                    num = int(num)
                except:
                    print("I did not understand your response please try again", sep='',end='\n') 
                print("Enter the range of numbers(lowest than highest): ")
                try:
                    low = int(input())
                    high = int(input())
                    tryloop = False
                except:
                    print("I did not understand your response please try again", sep='',end='\n')
            for x in range(num):
                print(random.randrange(low,high))
def main():
    loop = True
    while(loop):
        choice = menu()
        if(choice == 1):
            add()
        elif(choice == 2):
            subtract()
        elif(choice == 3):
            multiply()
        elif(choice == 4):
            divide()
        elif(choice == 5):
            power()
        elif(choice == 6):
            root()
        elif(choice == 7):
            rand()
main()