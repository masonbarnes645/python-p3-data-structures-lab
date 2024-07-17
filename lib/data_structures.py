

spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
    
]



def get_names(spicy_foods):
    names = []
    for food in spicy_foods:
        names.append(food.get('name'))
    return names

def get_spiciest_foods(spicy_foods):
    names = []
    for food in spicy_foods:
        if food.get('heat_level') > 5:
            names.append(food)
    return names

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        print(f"{food.get('name')} ({food.get('cuisine')}) | Heat Level: {'🌶'*food.get('heat_level')}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    names = []
    for food in spicy_foods:
        if food.get('cuisine') == cuisine:
            return food
def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        if food.get('heat_level') > 5:
            print(f"{food.get('name')} ({food.get('cuisine')}) | Heat Level: {'🌶'*food.get('heat_level')}")
            

def get_average_heat_level(spicy_foods):
    food_list_len = len(spicy_foods)
    total = 0
    for food in spicy_foods:
        total += food.get('heat_level')
    return (total/food_list_len)


def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods

get_spicy_food_by_cuisine(spicy_foods,'American')