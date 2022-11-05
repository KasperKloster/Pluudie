import os, json
import pandas as pd

class Write:   
  def jsonRecipes(self) -> str:    
    filepath = os.getcwd() + '/src/files/recipes.csv'    
    df = pd.read_csv(filepath, sep=';')
    # # Set empty values (NaN)    
    df = df.fillna("")
    # # Cast to dict with index
    recipes = df.to_dict(orient='index')
    # # Looping through ingredients
    for recipe in recipes:
      # Convert string to a list of dicts      
      ingredients = json.loads(recipes[recipe]['ingredients'])
      # Set as value
      recipes[recipe]['ingredients'] = ingredients
      
    # Cast to JSON
    recipes = json.dumps(recipes, indent=4)
    # Save JSON file    
    filepath = os.getcwd() + "/src/database/data/recipes.json"
    with open(filepath, "w") as outfile:
      outfile.write(recipes) 
    
    return filepath