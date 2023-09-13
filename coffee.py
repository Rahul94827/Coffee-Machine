
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 60.0,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 90.0,
        },
        "cost": 90.0,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 130.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def report():
    water=resources['water']
    milk=resources['milk']
    coffee=resources['coffee']

    print(f"Water:{water}\nMilk:{milk}\nCoffee:{coffee}")

def selection(ch):
    cash=int(input(("Please Enter the number of cash")))
    cost=MENU[ch]['cost']
    if cash<cost:
      print("Insufficient balance to place the order")

    else:
        ingredient = MENU[ch]['ingredients']
        for item, quantity in ingredient.items():
            if (resources[item]<=quantity):
                print(f"Sorry there is insufficient ingredient,Please collect your cash of {cash}")
                break
        else:
            for item, quantity in ingredient.items():
                resources[item] -= quantity
            if cash==cost:
                print(f"Here is your {ch},Enjoy ")

            else:
                re_cash=cash-cost
                print(f"Collect you change {re_cash}")
                print(f"Here is your {ch},Enjoy ")



def main():
    flag=True

    while flag:
        ch=input("What would you like? (espresso/latte/cappuccino)")
        if ch=='report':
            report()
        elif ch=='off':
            flag=False
        elif ch in MENU:
            selection(ch)
        else:
            print("Invalid Choice")
main()

