from lib.csv.Csv import Csv
from database.firebase.Firebase import Firebase
from lib.Recipe import Recipe
from lib.google.sheets import GoogleSheets

class Main:
  def __init__(self) -> None:     
    recipeFilePath = self.recipesData()    
    self.firebase(recipeFilePath)
    lists = self.selectRecipes()
    self.saveInGoogleDrive(lists)
    
  def recipesData(self) -> str:
    csv = Csv()
    recipeFilePath = csv.writeJsonRecipes()    
    return recipeFilePath
  
  def firebase(self, recipeFilePath:str):    
    firebase = Firebase()
    firebase.setRecipes(recipeFilePath)
  
  def selectRecipes(self) -> list[list[dict]]:
    recipes = Recipe()
    csv = Csv()
    weekRecipes = recipes.getRandom()
    shoppingList = recipes.createShoppinglist(weekRecipes)
    # csv.saveWeekPlan(weekRecipes)
    return [weekRecipes, shoppingList]
  
  def saveInGoogleDrive(self, lists):
    GoogleSheets(lists)



if __name__ == '__main__':
  Main()