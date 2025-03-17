# [] create list-o-matic as a function and call it
# [] be sure to include your spelled-out name in the welcome prompt
# [] you are welcome to use any list you like for list-o-matic, does not have to be animals 
# [] Harrison Zaharogiannis 

def list_o_matic(user_input, item_list):
    if user_input == "":
        if item_list:
            popped_item = item_list.pop()
            return popped_item, "popped from list"
        else:
            return "The list is empty!"
    
    if user_input == "quit":
        return "Goodbye!"
    
    if user_input in item_list:
        item_list.remove(user_input)
        return "1 instance of", user_input, "removed from list"
    
    item_list.append(user_input)
    return "1 instance of", user_input, "appended to list"

def main():
    animals = ['dog', 'rabbit', 'cat']
    name = "Harrison Zaharogiannis"  
    print("Welcome,", name, ". Look at all the animals", animals)

    while True:
        user_input = input('Enter the name of an animal or type "quit" to exit: ').strip().lower()
        result = list_o_matic(user_input, animals)
        print(result)
        
        if result == "Goodbye!":
            break
        print("Current list: ", animals)


main()
