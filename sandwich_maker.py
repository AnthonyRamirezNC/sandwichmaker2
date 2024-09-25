
class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = resources

    #method to check if machine has enough passed in ingredients
    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for key in ingredients.keys():
            if ingredients.get(key) > self.machine_resources[key]:
                #not enough to make it
                return False
            
        return True

    #method to make remove ingredients from resources and make sandwich
    def make_sandwich(self, sandwich_size, order_ingredients):
        for key in order_ingredients.keys():
            self.machine_resources[key] -= order_ingredients.get(key)
        print(f'{sandwich_size} sandwich is ready. Bon appetit!')