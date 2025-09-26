# lib/data_structures.py

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

# 1. Return a list of names of all spicy foods
def get_names(spicy_foods):
    return [food["name"] for food in spicy_foods]

# 2. Return a list of foods with heat_level > 5
def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food["heat_level"] > 5]

# 3. Print each food in the format: Name (Cuisine) | Heat Level: 🌶🌶🌶...
def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}")

# 4. Return a single dictionary for a food by its cuisine
def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food 

# 5. Print only the spiciest foods (heat_level > 5) in the same format
def print_spiciest_foods(spicy_foods):
    spiciest = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spiciest)

# 6. Return the average heat level (integer) of all foods
def get_average_heat_level(spicy_foods):
    total_heat = sum(food["heat_level"] for food in spicy_foods)
    return total_heat // len(spicy_foods)

# 7. Add a new spicy food dictionary to the list and return the updated list
def create_spicy_food(spicy_foods, new_spicy_food):
    spicy_foods.append(new_spicy_food)
    return spicy_foods
