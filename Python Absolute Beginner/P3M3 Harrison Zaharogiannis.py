# [ ] create fucntion, call and test 
# Define the cheese order function
# Harrison Zaharogiannis Module 3

def cheese_order(name, order_amount, max_order=69, min_order=0.5, price_per_lb=9.99):
    order_amount = float(order_amount)
    
    if order_amount > max_order:
        print(full_name, "more than currently available stock")
    elif order_amount < min_order:
        print(full_name, "below minimum order amount")
    else:
        total_price = order_amount * price_per_lb
        print(full_name, order_amount, 'lbs of cheese costs $', total_price)

full_name = input("Your full name goes here: ")
order_weight = input("Enter cheese order weight (numeric value): ") 

cheese_order(full_name, order_weight)
