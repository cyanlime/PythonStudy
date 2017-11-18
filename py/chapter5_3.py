#!/usr/bin/env python 3.1

def make_omelet_q3(fridge, omelet_type="mozzarella"):
    if type(fridge)!=type({}):
        raise TypeError("Bridge type is %s, not a dictionary" % type(fridge))
    return fridge

    if type(omelet_type)==type({}):
        print "Omelet_type is a dictionary with ingredients"
        return make_food(omelet_type, "omelet")
    if type(omelet_type)==type(""):
        omelet_ingredients = get_omelet_ingredients(omelet_type)
        return make_food(omelet_ingredients, omelet_type)
    else:
        print("I don't think I can make this kind of omelet: %s" % omelet_type)

    def get_omelet_ingredients(omelet_name):
        ingredients = {"eggs":2, "milk":1}
        if omelet_name == "cheese":
            ingredients["cheddar"] = 2
        elif omelet_name == "western":
            ingredients["jack_cheese"] = 2
            ingredients["ham"] = 1
        elif omelet_name == "mozzarella":
            ingredients["mushroom"] = 1
        else:
            print "Sorry, that's not on the menu"
            return None
        return ingredients
    

    def remove_from_fridge(ingredients_needed, fridge):
        recipe_ingredients = {}
        for ingredient in ingredients_needed.keys():
            if ingredient not in fridge.keys() or ingredients_needed[ingredient]>fridge[ingredient]:
                raise LookupError("ingredient %s not enough" % ingredient)
            fridge[ingredient]-=ingredients_needed[ingredient]
            recipe_ingredients[ingredient] = ingredients_needed[ingredient]
        return recipe_ingredients

    def make_food(ingredients_needed, food_name):
        for ingredient in ingredients_needed.keys():      
            print "Adding %d of %s to make a %s" % (ingredients_needed[ingredient], ingredient, food_name)
        print ("Made %s" % food_name)
        return food_name


if __name__ == "__main__":
    fridge = {"eggs": 3, "milk":3, "cheddar":10, "mushroom":4}
    make_omelet_q3(fridge)
    needed_ingredients = get_omelet_ingredients(mozzarella)
    recipe = remove_from_fridge(need_ingredients, fridge)
    print recipe





