# Tulip Bubble Game

# Constants
# coin_amt_dict = {
#   "fl50_amt": 12,
#   "fl25_amt": 12,
#   "fl10_amt": 24,
#   "fl05_amt": 24,
#   "fl01_amt": 48
# }

# tulip_price_level_dict = {
#   # Price level 1-7, each slot occupied once at a time
#   # change to colors using list combiner thing
#   "red":0,
#   "orange":0,
#   "white":0
# }

# colors = ['red','orange','white']

# Objects
class Player:
  def __init__(self, name, coins=20, tokens=3, hand=[]):
    self.name = name
    self.coins = coins
    self.tokens = tokens
    self.hand = hand

  def addCoin(self, amt):
    if amt > 0:
      self.coins += amt
    else:
      print("Amount must be positive")

  def spendCoin(self, amt):
    if self.coins > amt:
      self.coins -= amt
    else:
      print("Not enough coins")

  def addHand(self, flower):
    self.hand.append(flower)

  def __str__(self):
    return f"Player {self.name} has {self.coins} coins"
  
class Flower:
  def __init__(self, color, alpha, num, var):
    self.color = color
    self.alpha = alpha
    self.num = num
    self.var = var

  def __str__(self):
    return f"{self.color} {self.alpha}{self.num}v{self.var}"

# Initialization
def makeFlowers(colors, codes):
  return 0

# Console
red = Player("Vincent")

a = [Flower("red", "A", 1, 1),
     Flower("red", "A", 1, 2)]

for flower in a:
  red.addHand(flower)

for item in red.hand:
  print(item)

  me and the homies use gitlab