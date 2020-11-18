import time
options = ("1: Add name\n2: Display List\n3: Quit")
namesArray = ["","","","","","","","","",""]
choice = 0
while choice!= 3:
    print(options)
    try:
        choice = int(input("What would you like to do"))
    except ValueError:
        print("Not a choice, please re-enter")
    if choice == 1:
        name = input("What name would you like to add to the list?")
        try:
            pos = int(input("Where would you like to input the name? (1-10)"))
        except ValueError:
            print("Not a number, please re-enter")
        pos -= 1
        namesArray.insert(pos,name)
    if choice == 2:
        print("Printing List...")
        time.sleep(0.4)
        count = 1
        for i in namesArray:
            if i != "":
                print(count,":",i)
            else:
                print(count,": empty")
            count += 1
        time.sleep(0.4)
        print("\n")
            
        
        
time.sleep(0.5)
print("Program Terminating...")
