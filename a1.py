"""
CSSE1001 Assignment 1
Semester 1, 2023
"""

__author__ = "Lachlan Zakaras"
__email__ = "l.zakaras@uqconnect.edu.au"
__date__ = "03/03/2023"

from constants import *

def num_hours() -> float:
    """Return the hours spent in this assignment.

    >>> num_hours()
    12
    """
    hours_spent = 12.0

    return hours_spent

def get_recipe_name(recipe: tuple[str, str]) -> str:
    """Return the name of the recipe.

    Parameters:
        recipe[0] contains the name of the recipe

    >>> get_recipe_name(CHOCOLATE_PEANUT_BUTTER_SHAKE)
    'chocolate peanut butter banana shake'
    """

    return recipe[0]

def parse_ingredient(raw_ingredient_detail: str) -> tuple[float, str, str]:
    """Return the ingredients inputted as a tuple in correct data type.

    Parameters:
        Expect the user input to format as "amount measure ingredient"
 
    >>> parse_ingredient("1 cup flour")
    [1.0, "cup", "flour"]
    """
    ingredient_breakdown = raw_ingredient_detail.split(' ', 2)
    ingredient_breakdown[0] = float(ingredient_breakdown[0])
    ingredient_breakdown = tuple(ingredient_breakdown)

    return ingredient_breakdown

def create_recipe() -> tuple[str, str]:
    """Return a created recipe based on values entered by user
    
    >>> create_recipe()
    Please enter the recipe name: juice
    Please enter an ingredient: 0.5 cup lemon
    Please enter an ingredient: 5 g sugar
    Please enter an ingredient: 
    ('juice', '0.5 cup lemon,5 g sugar')
    """
    recipe_name = input("Please enter the recipe name: ")
    ingredient_string = ""

    while True:
        ingredient_name = input("Please enter an ingredient: ")

        if ingredient_name == "":
            ingredient_string = ingredient_string[:-1]
            break

        ingredient_string += ingredient_name + ","

    recipe = (recipe_name, ingredient_string)

    return recipe

def recipe_ingredients(recipe: tuple[str, str]) -> tuple([tuple
                                                         [float, str, str]]):
    """Return the ingredients of a recipe; amount, measure, ingredient.

    Parameters:
        recipe ingredients are in a csv format
    
    >>> recipe_ingredients(CHOCOLATE_PEANUT_BUTTER_SHAKE)
    (('1 large banana,2 tbsp peanut butter,2 pitted dates,1 tbsp cacao 
    powder,240 ml almond milk,0.5 cup ice,1 tbsp cocao nibs,1 tbsp flax seed'))
    """
    ingredients = list()

    split_ingredients = recipe[1].split(",")

    for num_ingredient in range(len(split_ingredients)):
        ingredients_tuple = parse_ingredient(split_ingredients
                                                       [num_ingredient])
        ingredients.append(ingredients_tuple)

    return tuple(ingredients)

def add_recipe(new_recipe: tuple[str, str], 
               recipes: list[tuple[str, str]]) -> None:
    """Appends a recipe to the 'recipes' list.

    >>> add_recipe(BROWNIE, recipes)
    >>> recipes
    [('chocolate brownies',
	'2 tbsp flaxseed,200 g dark chocolate,0.5 tsp coffee granules,
    80 g Nuttelex,125 g self-raising flour,70 g ground almonds,
    50 g cocoa powder,0.2 tsp baking powder,250 g sugar,
    1.5 tsp vanilla extract')]
    """
    recipes.append(new_recipe)

    return None

def find_recipe(recipe_name: str, 
                recipes: list[tuple[str, str]]) -> (tuple[str, str] | None):
    """Return the recipe if found based on user search. If not, return None.
    
    >>> find_recipe(BROWNIE, recipes)
    ('chocolate brownies',
    '2 tbsp flaxseed,200 g dark chocolate,0.5 tsp coffee granules,
    80 g Nuttelex,125 g self-raising flour,70 g ground almonds,
    50 g cocoa powder,0.2 tsp baking powder,250 g sugar,
    1.5 tsp vanilla extract')
    """

    for position in range(len(recipes)):
        for find_name in recipes[position]:
            if find_name == recipe_name:
                return recipes[position] 
    
    return None

def remove_recipe(name: str, recipes: list[tuple[str, str]]) -> None:
    """Remove a recipe from the list 'recipes'.
    
    >>> remove_recipe(...)
    """
    for position in range(len(recipes)):
        for find_name in recipes[position]:
            if find_name == name:
                recipes.pop(position)
                return None
    return None

def get_ingredient_amount(ingredient: str, recipe: 
                          tuple[str, str]) -> (tuple[float, str] | None):
    """Return ingredient amount and measure of specified ingredient 
    with a recipe.
    
    >>> get_ingredient_amount('peanuts', ('peanut butter', 
    '300 g peanuts,0.5 tsp salt,2 tsp oil'))
    (300.0, 'g')
    """
    ingredients = recipe_ingredients(recipe)

    for ingredient_name in ingredients:
        if ingredient_name[2] == ingredient:
            print(ingredient_name[0], ingredient_name[1])
            quantity, measure = ingredient_name[0], ingredient_name[1]
            check = True
            break
        else:
            check = False

    if not check:
        return None
    else:
        quantity_float = float(quantity)
        ingredient_amount = (quantity_float, measure)
        return ingredient_amount

def add_to_shopping_list(ingredient_details: tuple[float, str, str], 
                         shopping_list:
                         list[tuple[float, str, str] | None]) -> None:
    """Return the amount and measure of a certain ingredient.
    
    >>> shopping_list = [(300.0, 'g', 'peanuts'), (0.5, 'tsp', 'salt'),
    (2.0, 'tsp', 'oil')]
    >>> add_to_shopping_list((1000.0, 'g', 'tofu'), shopping_list)
    >>> shopping_list
    [(300.0, 'g', 'peanuts'), (0.5, 'tsp', 'salt'), (2.0, 'tsp', 'oil'),
    (1000.0, 'g', 'tofu')]
    """
    for ingredient in shopping_list:
        if ingredient[2] == ingredient_details[2]:
            added_quantity = ((ingredient[0] + ingredient_details[0]),
                                ingredient[1], ingredient[2])
            shopping_list.remove(ingredient)
            shopping_list.append(added_quantity)
            return None

    shopping_list.append(ingredient_details)
    return None

def remove_from_shopping_list(ingredient_name: str, amount: float,
                              shopping_list: list) -> None:
    """Remove ingredients from shopping list or reduce ingredient amount.
    
    >>> shopping_list = [(1500.0, 'g', 'peanuts'), (0.5, 'tsp', 'salt'),
    (2.0, 'tsp', 'oil'), (9000.0, 'g', 'tofu'), (100.0, 'g', 'sugar'),
    (50.0, 'g', 'tomato sauce'), (120.0, 'g', 'rice'),
    (920.0, 'g', 'ice cream')]
    >>> remove_from_shopping_list('ice cream', 500.0, shopping_list)
    >>> shopping_list
    [(1500.0, 'g', 'peanuts'), (0.5, 'tsp', 'salt'), (2.0, 'tsp', 'oil'),
    (9000.0, 'g', 'tofu'), (100.0, 'g', 'sugar'), (50.0, 'g', 'tomato
    sauce'), (120.0, 'g', 'rice'), (420.0, 'g', 'ice cream')]
    """
    for ingredient in shopping_list:
        if ingredient[2] == ingredient_name and (ingredient[0] - amount) > 0:
            subtracted_quantity = ((ingredient[0] - amount), ingredient[1],
                                    ingredient[2])
            shopping_list.remove(ingredient)
            shopping_list.append(subtracted_quantity)
        elif ingredient[2] == ingredient_name and (ingredient[0]
                                                   - amount) <= 0:
            shopping_list.remove(ingredient)

    return None

def generate_shopping_list(recipes: 
                           list[tuple[str, str]]) -> (list[tuple
                                                     [float, str, str]]):
    """Returns a list of ingredients, given the list of recipes.
    
    >>> shopping_list = generate_shopping_list([PEANUT_BUTTER,
    MUNG_BEAN_OMELETTE])
    >>> shopping_list
    [(300.0, 'g', 'peanuts'), (1.0, 'tsp', 'salt'), (3.0, 'tsp', 'oil'),
    (1.0, 'cup', 'mung bean'), (0.75, 'tsp', 'pink salt'), (0.25, 'tsp',
    'garlic powder'), (0.25, 'tsp', 'onion powder'), (0.125, 'tsp',
    'pepper'), (0.25, 'tsp', 'turmeric'), (1.0, 'cup', 'soy milk')]
    """
    shopping_list = []
    
    for recipe in recipes:
        ingredients = recipe_ingredients(recipe)
        for details in ingredients:
            add_to_shopping_list(details, shopping_list)

    return shopping_list

def display_ingredients(shopping_list: list[tuple[float, str, str]]) -> None:
    """Print the shopping list in the specified structure.

    >>> display_ingredients([(1.0, 'large', 'banana'), (0.5, 'cup', 'ice'),])
    | 1.0 | large | banana |
    | 0.5 | cup | ice |
    """
    shopping_list_amounts_str = []
    for amount in shopping_list:
        shopping_list_amounts_str.append(str(amount[0]))

    longest_amount = len(max(shopping_list_amounts_str, key=len))
    longest_measure = len(max(shopping_list, key=lambda x: len(x[1]))[1])
    longest_ingredient = len(max(shopping_list, key=lambda x: len(x[2]))[2])    

    # identifies required spaces for the middle buffer, depending on whether
    # the string length is even or odd.
    measure_buffer = []
    for measure in shopping_list:
        required_buffer = longest_measure - len(measure[1])
        if len(measure[1]) % 2 == 0:
            even_buffer = int(required_buffer/2)
            measure_buffer.append(" " + " "*even_buffer + measure[1] 
                                  + " "*even_buffer + "  ")
        elif required_buffer == 0:
            measure_buffer.append(" " + measure[1] + "  ")
        else:
            left_buffer = required_buffer//2 + 1
            right_buffer = required_buffer - left_buffer
            measure_buffer.append(" " + " "*left_buffer + measure[1]
                                  + " "*right_buffer + "  ")   

    # added spaces next to "|" to accomadate for required spaces.
    for position in range(len(shopping_list)):
        result = ("| " + str(shopping_list[position][0]).rjust(longest_amount) 
        + " |" + measure_buffer[position] + "| " 
        + str(shopping_list[position][2]).ljust(longest_ingredient) + "  |")
        print(result)

    return None

def sanitise_command(command: str) -> str:
    """Return a standardised command to all lowercase, no digits and no
    leading/trailing white space.
    
    >>> sanitise_command('add chocolate Brownies 5')
    'add chocolate brownies'
    """
    sanitised_command = command.lower()
    sanitised_command = sanitised_command.strip()

    for char in sanitised_command:
        if char in "1234567890":
            sanitised_command = sanitised_command.replace(char, "")

    return sanitised_command

def main() -> None:
    """Runs when file is open prompts for user interaction to run functions."""
    # cook book
    recipe_collection = [
        CHOCOLATE_PEANUT_BUTTER_SHAKE,
        BROWNIE,
        SEITAN,
        CINNAMON_ROLLS,
        PEANUT_BUTTER, 
        MUNG_BEAN_OMELETTE
    ]

    # creates list to store recipes in upcoming functions
    recipes = []

    # creates list to store shopping list in upcoming functions
    shopping_list = []

    while True:
        user_input = input("Please enter a command: ")

        if sanitise_command(user_input) == "q":
            break
        elif sanitise_command(user_input) == "h":
            print(HELP_TEXT)
        elif sanitise_command(user_input) == "ls":
            if len(recipes) > 0:
                print(recipes)
            else:
                print("No recipe in meal plan yet.")
        elif sanitise_command(user_input) == "ls -a":
            for recipe in recipe_collection:
                print(recipe[0])
        elif sanitise_command(user_input)[:3] == "add": 
            _, recipe_name = sanitise_command(user_input).split(" ",1)
            found_check = False
            for recipe in recipe_collection:
                if recipe[0] == recipe_name:
                    add_recipe(recipe, recipes)
                    found_check = True
            if not found_check:
                print("\nRecipe does not exist in the cook book. \n" \
                        "Use the mkrec command to create a new recipe.\n")
        elif sanitise_command(user_input) == "g": 
            shopping_list = generate_shopping_list(recipes)
            if len(shopping_list)>0:
                display_ingredients(shopping_list)
        elif user_input[:5] == "rm -i":
            ingredient_name, amount = user_input[6:].rsplit(" ",1)
            remove_from_shopping_list(ingredient_name, float(amount),
                                      shopping_list)
        elif sanitise_command(user_input)[:2] == "rm":
            _, recipe_name = sanitise_command(user_input).split(" ",1)
            remove_recipe(find_recipe(recipe_name, recipes), recipes)
        elif sanitise_command(user_input) == "ls -s":
            display_ingredients(shopping_list)
        elif sanitise_command(user_input) == "mkrec":
            recipe_collection.append(create_recipe())

if __name__ == "__main__":
    main()