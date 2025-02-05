# [ ] create, call and test fishstore() function 
def fishstore(fish, price):
    return "The fish", fish, " is available for $" + str(price)

name = "Harrison Zaharogiannis"
fish_entry = input("Type of fish: ")
price_entry = input("Whats the price? ")

print("Report for", name, fishstore(fish_entry, price_entry))