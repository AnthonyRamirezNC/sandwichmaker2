class Cashier:
    def __init__(self):
        pass

    #method to process coin input
    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        coinAmount  = 0
        print("Please insert coins")
        coinAmount += int(input("how many large dollars?: "))
        coinAmount += (.5 * int(input("how many half dollars?: ")))
        coinAmount += (.25 * int(input("how many quarters?: ")))
        coinAmount += (.05 * int(input("how many nickels?: ")))
        return coinAmount
    
    #method to get result from transaction
    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if coins < cost:
            return False
        else: 
            change = coins - cost
            print(f'Here is ${change} in change')
            return True
