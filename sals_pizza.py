# To keep track of the kinds of pizzas I sell, 
# I created a list called toppings that holds the following --
toppings = ["pepperoni", "buffalo chicken", "cheese", "sausage", "meat lovers", "anchovies", "hamburger"]

# To keep track of how much each kind of pizza slice costs, 
# I created a list called prices that holds the following integer values --
prices = [2, 6, 1, 3, 2, 7, 2]

# Counting the number of occurrences of 2 in the prices list, 
# and storing the result in a variable called twoDollarSlices.
twoDollarSlices = prices.count(2)
print(twoDollarSlices)

# OUTPUT: 3

# Finding the length of the toppings list and storing it in a variable
# called numberOfPizzas
numberOfPizzas = len(toppings)
print(numberOfPizzas)

# OUTPUT: 7

# Printing a string where numberOfPizzas represents the value of my variable numberOfPizzas --
print("We sell " + str(numberOfPizzas) + " different kinds of pizza!")

# OUTPUT: We sell 7 different kinds of pizza!

# Creating a new two-dimensional list called pizzaAndPrices from existing data --
pizzaAndPrices = [
  [2, "pepperoni"],
  [6, "buffalo chicken"],
  [1, "cheese"],
  [3, "sausage"],
  [2, "meat lovers"],
  [7, "anchovies"],
  [2, "hamburger"]
]

# Sorting pizzaAndPrices so that the pizzas are in order of increasing price (ascending).
pizzaAndPrices.sort()
print(pizzaAndPrices)

# OUTPUT: [
#   [1, 'cheese'], 
#   [2, 'hamburger'], 
#   [2, 'meat lovers'], 
#   [2, 'pepperoni'], 
#   [3, 'sausage'], 
#   [6, 'buffalo chicken'], 
#   [7, 'anchovies']
# ]

# Storing the first element of pizzaAndPrices in a variable called cheapestPizza --
cheapestPizza = pizzaAndPrices[0]
print(cheapestPizza)

# OUTPUT: [1, 'cheese']

# Storing an element of pizzaAndPrices in a variable called priciestPizza --
priciestPizza = pizzaAndPrices[-1]
print(priciestPizza)

# OUTPUT: [7, 'anchovies']

# Removing the priciestPizza from the list --
pizzaAndPrices.remove([7, "anchovies"])
print(pizzaAndPrices)

# OUTPUT: [
#   [1, 'cheese'], 
#   [2, 'hamburger'], 
#   [2, 'meat lovers'], 
#   [2, 'pepperoni'], 
#   [3, 'sausage'], 
#   [6, 'buffalo chicken']
# ]

# Since I'm all out of anchovies, I'll be adding a new topping --
pizzaAndPrices.insert(4, [2.5, "chicken parm"])
print(pizzaAndPrices)

# OUTPUT: [
#   [1, 'cheese'], 
#   [2, 'hamburger'], 
#   [2, 'meat lovers'], 
#   [2, 'pepperoni'], 
#   [2.5, 'chicken parm'], 
#   [3, 'sausage'], 
#   [6, 'buffalo chicken']
# ]

# The friggin' NINJA TURTLES sneaked their way into my pizza shop right after closing!!
# They ain't got any money, so I slice up the pizzaAndPrices list and store
# the 4 cheapest pizzas in a list called fourCheapest.
fourCheapest = pizzaAndPrices[:4]
print(fourCheapest)

# OUTPUT: [
#   [1, 'cheese'], 
#   [2, 'hamburger'], 
#   [2, 'meat lovers'], 
#   [2, 'pepperoni']
# ]