import os, json

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

class Firebase:
  def __init__(self) -> None:    
    databaseUrl = 'https://pluudie-default-rtdb.europe-west1.firebasedatabase.app/'
    cred = credentials.Certificate(os.getcwd() + "/src/database/firebase/credentials/serviceAccountKey.json")
    firebase_admin.initialize_app(cred, {
      'databaseURL': databaseUrl
    })
  
  """
  Setting will create a new database
  """
  def setRecipes(self, recipeFilePath):
    # Which firestore database
    ref = db.reference("recipes")
    # Opening JSON file
    with open(recipeFilePath, 'r') as openfile:
      # Reading from json file
      json_object = json.load(openfile)
    # Set in the database
    ref.set(json_object)
  
  def setUnits(self):
    ref = db.reference('units')
    with open(os.getcwd() + '/src/database/data/units.json', 'r') as openfile:
      # Reading from json file
      json_object = json.load(openfile)
    # Set in the database
    ref.set(json_object)

