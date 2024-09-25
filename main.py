import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


#helper methods to reduce repeating of input code
def processInput(cashier, sandwichMaker, userInput):

    #check if resources are sufficient to make passed in recipe
    if(sandwichMaker.check_resources(recipes[userInput]["ingredients"])):
        #able to make recipe
        #process coin input
        coins = cashier.process_coins()

        #process transaction
        if(cashier.transaction_result(coins, recipes[userInput].get("cost"))):

            #make the resource
            sandwichMaker.make_sandwich(userInput, recipes[userInput]["ingredients"])
        else:
            print("Sorry that's not enough money. Money refunded.")
    else:
        print("Sorry there is not enough resources")

#method to print amount of each ingradient
def printReport():
    for key in sandwich_maker_instance.machine_resources.keys():
        if key == "ham":
            print(f'Ham: {sandwich_maker_instance.machine_resources.get(key)} slice(s)')
        elif key == "bread":
            print(f'Bread: {sandwich_maker_instance.machine_resources.get(key)} slice(s)')
        else:
            print(f'Cheese: {sandwich_maker_instance.machine_resources.get(key)} pound(s)')


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()




def main():
    ###  write the rest of the codes ###
    userInput = ""

    while(userInput != "off"):
        userInput = input("What would you like? (small/ medium/ large/ off/ report): ")
        if(userInput == "small"):
            processInput(cashier_instance, sandwich_maker_instance, userInput)

        elif(userInput == "medium"):
            #check if resources are sufficient
            processInput(cashier_instance, sandwich_maker_instance, userInput)

        elif(userInput == "large"):
            #check if resources are sufficient
            processInput(cashier_instance, sandwich_maker_instance, userInput)
        
        elif(userInput == "report"):
            #check if resources are sufficient
            printReport()

        elif(userInput == "off"):
            break
        else: 
            print("Invalid User Input")

if __name__=="__main__":
    main()
