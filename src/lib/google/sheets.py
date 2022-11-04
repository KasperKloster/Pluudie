import gspread, os

class GoogleSheets:
  def __init__(self, lists : list[list[dict]]) -> None:    
    # connect to service account
    serviceAccount = gspread.service_account(filename = os.getcwd() + '/src/lib/google/credentials/service_account.json')
    # Connect to sheet
    self.sheet = serviceAccount.open("WeekPlan")
    # Save weekplan
    self.saveWeekPlan(weekplan = lists[0])
    # Save shoppinglist
    self.saveShoppingList(shoppingList = lists[1])

  def saveWeekPlan(self, weekplan : list[dict]) -> None:      
    # Worksheet  
    weekPlanSheet = self.sheet.worksheet("Weekplan")    
    for i, recipe in enumerate(weekplan):            
      # Updating names
      weekPlanSheet.update('B' + str(2 + i), recipe['name'])
      # Updating links
      weekPlanSheet.update('C' + str(2 + i), recipe['link'])
      # Updating ingredients
      weekPlanSheet.update('D' + str(2 + i), str(recipe['ingredients']))
  
  def saveShoppingList(self, shoppingList : list[dict]) -> None:
    # Worksheet  
    shoppingListSheet = self.sheet.worksheet("Shoppinglist")    
    for i, item in enumerate(shoppingList):      
      # Updating amount
      shoppingListSheet.update('A' + str(2 + i), item['amount'])
      shoppingListSheet.update('B' + str(2 + i), item['name'])