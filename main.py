from menu import menu, resources

water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]
money = resources["money"]

def buyCoffee():
    userInput = int(input('''
_________________________________________
What would you like to do?
1. Buy Coffee
2. Get Report
_________________________________________
    '''))
    print("_________________________________________")

    def calcResources(ingredient, input_type):
        global water, milk, coffee, money

        if input_type == 1:
            menu_item = menu[ingredient]
            cost = menu_item["cost"]
            ingredients = menu_item["ingredients"]
            newWater = water - ingredients["water"]
            newCoffee = coffee - ingredients["coffee"]
            newMoney = money - cost

            if newWater < 0 or newCoffee < 0:
                print("Insufficient resources. Sorry!")
                return

            water = newWater
            coffee = newCoffee
            money = newMoney
            print(f"Your {ingredient} coffee is ready, enjoy!")

        elif input_type in [2, 3]:
            menu_item = menu[ingredient]
            cost = menu_item["cost"]
            ingredients = menu_item["ingredients"]
            newWater = water - ingredients["water"]
            newMilk = milk - ingredients["milk"]
            newCoffee = coffee - ingredients["coffee"]
            newMoney = money - cost

            if newWater <= 0 or newMilk <= 0 or newCoffee <= 0:
                print("Insufficient resources. Sorry!")
                print(f"Remaining resources: \nwater: {newWater}ml,  \nmilk: {newMilk}ml,  \ncoffee: {newCoffee}g,  \nmoney: ${newMoney}")
                exit()

            water = newWater
            milk = newMilk
            coffee = newCoffee
            money = newMoney

            print(f"Your {ingredient} coffee is ready, enjoy!")

        else:
            print("Invalid command")
            exit()

    if userInput == 1:
        coffeeType = int(input('''
What type of coffee would you like?
_________________________________________
1. espresso
2. latte
3. cappuccino
_________________________________________
        '''))
        print("_________________________________________")

        if coffeeType not in [1, 2, 3]:
            print("Invalid coffee type")
            exit()

        if coffeeType == 1:
            calcResources("espresso", 1)
        elif coffeeType == 2:
            calcResources("latte", 2)
        elif coffeeType == 3:
            calcResources("cappuccino", 3)

    elif userInput == 2:
        report = f"water: {water}ml \nmilk: {milk}ml \ncoffee: {coffee}g \nmoney: ${money} \n"
        print(report)

    else:
        print("Invalid command")
        exit()
buyCoffee()

shouldContinue = True
inputContinue = int(input('''
Would you like to get another coffee?
_________________________________________
1. yes
2. no
_________________________________________
'''))

while inputContinue == 1 and shouldContinue == True:
    buyCoffee()
if inputContinue == 2:
    exit()