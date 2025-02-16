# [ ] create, call and test the adding_report() function
# Harrison Zaharogiannis Python Absolute Beginner Module 5 FINAL Project

def adding_report(report="T"):
    total = 0
    items = ""
    
    print("Input an integer to add to the total or 'Q' to quit")
    
    while True:
        user_input = input("Enter an integer or 'Q': ").strip().upper()
        
        if user_input.isdigit():
            number = int(user_input)
            total += number
            if report == "A":
                items += str(number) + "\n"
        elif user_input.upper().startswith("Q"):
            if report == "A":
                print("\nItems")
                print(items)
            print("\nTotal")
            print(" ", total)
            print(" Calculated by: Harrison Zaharogiannis")
            break
        else:
            print(user_input + " is invalid input")

adding_report("A") 
adding_report("T")