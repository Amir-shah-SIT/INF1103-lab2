inventory = 0 
rejected = 0
quit = False
while quit == False :
    print("\nCurrent Stock is:" + str(inventory))
    userInput = input("Input additional stock value or quit:\n")
    if userInput.isdigit() == True:
        if int(userInput) < 0:
            rejected += 1
            print("\nUnacceptable input")
        else:
            inventory += int(userInput)
            if inventory > 500:
                rejectedStock = inventory -500
                inventory = 500
                print("\nInventory exceeds 500 limit quitting program")
                print("\nRejected Stock: " + str(rejectedStock))
                quit = True
        
    elif userInput.lower() == "quit":
        quit = True

    else:
        rejected += 1
        print("Unacceptable input")
        
print("\nTotal units added: " + str(inventory))
print("\nTotal rejected queries: " + str(rejected))    
    
