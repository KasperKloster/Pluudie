import gspread, os

class GoogleSheets:
  def __init__(self, weekRecipes : list[dict], shoppingList : list[dict]) -> None:    
    # connect to service account
    serviceAccount = gspread.service_account(filename = os.getcwd() + '/src/database/firebase/credentials/sheets.json')
    # Connect to sheet
    self.sheet = serviceAccount.open("WeekPlan")
    # Save weekplan
    self.saveWeekPlan(weekplan = weekRecipes)
    # Save shoppinglist
    self.saveShoppingList(shoppingList = shoppingList)

  def saveWeekPlan(self, weekplan : list[dict]) -> None:      
    # Worksheet  
    weekPlanSheet = self.sheet.worksheet("Weekplan")    
    for i, recipe in enumerate(weekplan):            
      # Updating names
      weekPlanSheet.update('B' + str(2 + i), recipe['name'])
      # Updating links
      weekPlanSheet.update('C' + str(2 + i), recipe['link'])
      
      # Working ingredients
      ingredients = []
      for ingredient in recipe['ingredients']:
        ingredients.append(str(ingredient['amount']) + " " + ingredient['unit'] + " " + ingredient['name'])
      
      # Updating ingredients
      weekPlanSheet.update('D' + str(2 + i), str(ingredients))
  
  def saveShoppingList(self, shoppingList : list[dict]) -> None:
    # Worksheet  
    shoppingListSheet = self.sheet.worksheet("Shoppinglist")    
    # Clear old shopping list
    shoppingListSheet.batch_clear(["A2:B99"])
    # Updating shopping list
    for i, item in enumerate(shoppingList):      
      # Updating amount
      shoppingListSheet.update('A' + str(2 + i), item['amount'])
      shoppingListSheet.update('B' + str(2 + i), item['name'])