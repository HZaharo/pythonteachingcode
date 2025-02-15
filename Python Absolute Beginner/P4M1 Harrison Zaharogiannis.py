# [ ] create, call and test the str_analysis() function  

def str_analysis(test_string):
    if test_string.isdigit():
        num = int(test_string)
        if num > 99:
            return test_string + " is a pretty big number"
        else:
            return test_string + " is a smaller number than expected"
    
    elif test_string.isalpha():
        return "\"" + test_string + "\"" + " is all alphabetical characters!"
    
    else:
        return "\"" + test_string + "\"" + " has multiple character types"

while True:
    user_input = input("Enter word or integer: ")
    
    if user_input.strip() != "":
        break
    else:
        print("Input cannot be empty, please try again.")


result = str_analysis(user_input)

print(result)
