import json

with open('coffee_menu.json', 'r') as file:
    menu = json.load(file)

print(menu['Menu']['cappuccino'])
print("Ingredients in espresso:", menu['Menu']['espresso']['ingredients'])
    