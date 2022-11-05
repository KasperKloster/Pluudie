from firebase_admin import db
import random

class Recipe:
  def getRandom(self) -> list[dict]:
    ref = db.reference("recipes").get()
    # Select 7 (k) random
    recipes = random.choices(ref, k = 7)
    return recipes