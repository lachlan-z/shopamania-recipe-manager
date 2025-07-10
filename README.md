# Shopamania Recipe Manager

A Python command-line application that helps manage recipes and automatically generates shopping lists based on selected meals for the week.

## Overview

Shopamania is designed for busy parents who need to efficiently plan their weekly grocery shopping. The application manages a cookbook of recipes and generates consolidated shopping lists by combining ingredients from multiple selected recipes.

## Features

- **Recipe Management**: Add, remove, and view recipes in your cookbook
- **Shopping List Generation**: Automatically combine ingredients from selected recipes
- **Ingredient Consolidation**: Intelligently merges duplicate ingredients with proper quantity calculations
- **Interactive Commands**: Easy-to-use command-line interface
- **Flexible Display**: View recipes, shopping lists, and available cookbook entries

## Commands

| Command | Description |
|---------|-------------|
| `h` or `H` | Display help message |
| `add {recipe}` | Add a recipe to your meal plan |
| `rm {recipe}` | Remove a recipe from your meal plan |
| `rm -i {ingredient} {amount}` | Remove specific amount of ingredient from shopping list |
| `ls` | List all recipes in current meal plan |
| `ls -a` | List all available recipes in cookbook |
| `ls -s` | Display current shopping list |
| `g` or `G` | Generate and display shopping list |
| `mkrec` | Create a new recipe interactively |
| `q` or `Q` | Quit the application |

## Usage

1. Run the program:
   ```bash
   python a1.py
   ```

2. Use commands to manage your recipes and shopping list:
   ```
   Please enter a command: add peanut butter
   Please enter a command: g
   | 300.0 | g   | peanuts |
   | 0.5   | tsp | salt    |
   | 2.0   | tsp | oil     |
   ```

3. Create new recipes:
   ```
   Please enter a command: mkrec
   Please enter the recipe name: smoothie
   Please enter an ingredient: 1 large banana
   Please enter an ingredient: 240 ml almond milk
   Please enter an ingredient: 
   ```

## Recipe Format

Recipes are stored as tuples containing:
- Recipe name (string)
- Ingredients (comma-separated string in format: "amount measure ingredient_name")

Example: `('peanut butter', '300 g peanuts,0.5 tsp salt,2 tsp oil')`

## Key Functions

- **Recipe Management**: Add, find, and remove recipes
- **Ingredient Parsing**: Parse ingredient strings into structured data
- **Shopping List Generation**: Combine ingredients from multiple recipes
- **Display Formatting**: Format shopping lists in aligned columns
- **Command Sanitization**: Clean and standardize user input

## Technical Details

- **Language**: Python 3.10+
- **Data Structures**: Uses tuples for recipes and lists for collections
- **No External Dependencies**: Built using only Python standard library
- **Input Validation**: Handles recipe names with only lowercase letters

## Development Notes

This project was developed as part of a software engineering course focusing on:
- Program design and structure
- Function decomposition
- Data type selection and manipulation
- User interface design
- Code documentation and testing

## File Structure

```
shopamania-recipe-manager/
├── a1.py              # Main application file
├── constants.py       # Pre-defined recipes and constants
└── README.md          # This file
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/lachlan-z/shopamania-recipe-manager.git
   cd shopamania-recipe-manager
   ```

2. Run the application:
   ```bash
   python a1.py
   ```

## Example Session

```
Please enter a command: add peanut butter
Please enter a command: add cinnamon rolls
Please enter a command: g
| 600.0 | g   | peanuts        |
| 1.5   | tsp | salt           |
| 4.0   | tsp | oil            |
| 510.0 | ml  | almond milk    |
| 285.0 | g   | Nuttelex       |
| 50.0  | g   | sugar          |
| 7.0   | g   | active dry yeast |
| 5.5   | cup | flour          |
| 165.0 | g   | brown sugar    |
| 2.0   | tbsp| cinnamon       |
| 160.0 | g   | powdered sugar |
| 0.5   | tsp | vanilla extract|
```

## License

This project is for educational purposes as part of a university assignment.