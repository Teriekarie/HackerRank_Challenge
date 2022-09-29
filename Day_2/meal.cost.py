# python program to find and print the meal's total cost.
#Given the meal price (base cost of a meal), tip percent (the percentage of the meal price being added as tip), and tax percent (the
# percentage of the meal price being added as tax) for a meal

# There are 3 lines of numeric input:

# The first line has a double, mealCost (the cost of the meal before tax and tip).
mealCost = float(input())

# The second line has an integer, tipPercent (the percentage of mealCost being added as tip). 
tipPercent = int(input())

# The third line has an integer, taxPercent (the percentage of mealCost being added as tax).
taxPercent = int(input())

#calculation
tip_cost = (tipPercent/100.)* mealCost
tax_cost = (taxPercent/100.)* mealCost
totalCost = int(round(mealCost + tip_cost + tax_cost))

print( "The total meal cost is", totalCost, "dollars." )