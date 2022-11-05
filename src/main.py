from database.data.write.Write import Write
from database.firebase.Firebase import Firebase
from lib.Recipe import Recipe
from lib.ShoppingList import ShoppingList
from lib.google.sheets import GoogleSheets

class Main:
  def __init__(self) -> None:         
    recipeFilePath = self.writeData()    
    self.firebase(recipeFilePath)    
    weekRecipes = self.selectRecipes()
    shoppingList = self.shoppingList(weekRecipes)
    self.saveInGoogleDrive(weekRecipes, shoppingList)
    
  def writeData(self) -> str:
    write = Write()
    recipeFilePath = write.jsonRecipes()    
    return recipeFilePath
  
  def firebase(self, recipeFilePath:str):    
    firebase = Firebase()
    firebase.setRecipes(recipeFilePath)
  
  def selectRecipes(self) -> list[dict]:
    recipes = Recipe()    
    weekRecipes = recipes.getRandom()     
    return weekRecipes
  
  def shoppingList(self, weekRecipes) -> list[dict]:
    sList = ShoppingList()    
    shoppingList = sList.createShoppinglist(weekRecipes)   
    return shoppingList
  
  def saveInGoogleDrive(self, weekRecipes, shoppingList):    
    GoogleSheets(weekRecipes, shoppingList)

if __name__ == '__main__':
  Main()