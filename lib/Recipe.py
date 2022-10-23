from firebase_admin import db
import random

class Recipe:
  def getRandom(self) -> list[dict]:
    ref = db.reference("recipes").get()
    # Select 7 (k) random
    recipes = random.choices(ref, k = 7)
    return recipes
  
  def createShoppinglist(self, recipes) -> list[dict]:
    # All ingredients name
    shopIngredientName : list[str] = []
    for recipe in recipes:
      for ingredient in recipe['ingredients']:
        # All names to list
        shopIngredientName.append(ingredient['name'])
        # remove duplicates from list
        shopIngredientName = list(dict.fromkeys(shopIngredientName))
    
    # creating a list of dicts with items
    shoppingListItems : list[dict] = []
    for name in shopIngredientName:
      shoppingListItems.append({'name' : name, 'amount' : 0})

    # Looping through recipes/ingredients again
    for recipe in recipes:
      for ingredient in recipe['ingredients']:
        # Looping through items in shoppingList
        for shopItem in shoppingListItems:
          # if what is in the ingredients has the same name as shoppingListItems
          if ingredient['name'] == shopItem['name']:
            # Add the amount
            shopItem['amount'] += ingredient['amount']

    return shoppingListItems