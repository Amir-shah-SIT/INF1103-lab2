inventory = 0 
rejected = 0
quit = False
while quit == False :
    print("\nCurrent Stock is:" + str(inventory))
    userInput = input("\nInput additional stock value or quit:\n")
    if userInput.isdigit() == True:
        if int(userInput) < 0:
            rejected += 1
            print("\nUnacceptable input")
        else:
            inventory += int(userInput)

            if inventory >=  500:
                rejectedStock = inventory - 500
                inventory = 500
                if(rejectedStock > 0):
                    print("\nInventory exceeds 500 limit quitting program")
                    print("\nRejected Stock: " + str(rejectedStock))
                else:
                    print("\nInventory has hit the limit of 500")
                break
        
    elif userInput.lower() == "quit":
        quit = True

    else:
        rejected += 1
        print("Unacceptable input")
        
print("\nTotal units added: " + str(inventory))
print("\nTotal rejected queries: " + str(rejected))    
    
