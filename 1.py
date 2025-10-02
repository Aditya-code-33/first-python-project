menu = {
    "Pizza":70,
    "Pasta":50,
    "Burger":30,
    "Salad":30,
    "Coffee":60
}

print("Hello Sir")
print("Welcome to our restaurant")
print("This is our MENU")
print("Pizza: 70/-\nPasta: 50/-\nBurger: 30/-\nSalad: 30/-\nCoffee: 60/-")
order_total = 0

item_1 = input("Enter an item to order: ").capitalize()
if item_1 in menu:
    order_total += menu[item_1]
    print(f"{item_1} has been added")
else:
    print("Sorry! That's not availale")
    
another_orderd=input("do you like to have another ordered sir (yes/no)")

if another_orderd=="yes":
    item_2=input("enter the second item for you")
    if item_2 in menu:
        order_total+=menu[item_2]
        print(f"ypur ordered {item_2}it has been placed")
    else:
        print("this item is not in our in restaurant")
        
else:
    print(f"your total bill is {order_total}")