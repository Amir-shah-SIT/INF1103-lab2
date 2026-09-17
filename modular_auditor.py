inventory = 0 
rejected = 0
quit = False

def get_valid_input():
    valid_input = False
    while valid_input == False: 
        global rejected
        userInput = input("\nInput additional stock value or quit:\n")
        if userInput.isdigit() == True:
            if int(userInput) < 0:
                rejected += 1
                print("\nUnacceptable input")
            else:
                return userInput
        elif userInput.lower() == "quit":
            return userInput.lower()
        else:
            rejected += 1
            print("Unacceptable input") 
    
def process_delivery(current_total, new_value):
    current_total += int(new_value)
    return current_total

def calculate_tax(amount):
    tax = amount *.10
    print("\n The tax amount is: $"+ str(tax))

def generate_report(total_units, failed_attempts):  
    print("\nTotal Deliveries Processed: " + str(total_units))
    print("\nNumber of Failed/Rejected Entries: " + str(failed_attempts))
    return 

while quit == False :
    print("\nTotal Deliveries Processed: " + str(inventory))
    accepted_Input = get_valid_input()
    if accepted_Input == 'quit':
        generate_report(inventory,rejected)
        calculate_tax(inventory)
        break
    else:
        inventory = process_delivery(inventory,accepted_Input)
        if inventory > 500:
            generate_report(500,rejected)
            print("\nNumber of Rejected Stock: "+ str(inventory-500))
            calculate_tax(500)
            break
        calculate_tax(inventory)
        
            
    


