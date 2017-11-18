#!/usr/bin/env python 3.1

a=10
b=20
print ("a added to b is %d" % (a+b))

def in_fridge():
    try:
        count= fridge[wanted_food]
    except keyError:
        count=0
    return count

def make_omelet(omelet_type):
    if type(omelet_type)==type({}):
        print("omelet_type is a dictionary with ingredients")
        return make_food(omelet_type, "omelet")
    elif type(omelet_type)==type("")
        omelet_ingredients = get_omelet_ingredients(omelet_type)
        return make_food(omelet_ingredients, omelet_type)
    else:
        print ("I don't think I can make this kind of omelet: %s" % omelet_type)

def make_food(ingredients_needed, food_name):
    for ingredient in ingredients_needed.keys():
        print("Adding %d of %s to make a %s" % (ingredients_needed[ingredient], ingredient, food_name))
    print("Made %s" % food_name)
    return food_name

def get_omelet_ingredients(omelet_name):
    ingredients = {"eggs":2, "milk":1}
    if omelet_name == "cheese":
        ingredients["cheddar"] = 2
    elif omelet_name == "western"
        ingredients["jack_cheese"] = 2
        ingredients["ham"] = 1
    elif omelet_name == "greek":
        ingredients["feta_cheese"] = 2
        ingredients["spinach"] = 2
    else:
        print("That's not on the menu, sorry!")
        return None
    return ingredients



if __name__ == '__main__':
    print ("a added to b is %d" % (a+b))
    fridge = {'apple':20, 'orange':10, 'milk':2}
    wanted_food = 'apple'
    print in_fridge()