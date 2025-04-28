# Car Salesman
# Total cost of a car purchase
dealerPrep = 500
destCharge = 200
tax = 0.2
license = 0.15

basePrice = int(input("Enter the base price of the car: "))
# Calculate the total cost
totalCost = basePrice + dealerPrep + destCharge + (basePrice * tax) + (basePrice * license)
# Print the total cost  
print("The total cost of the car is: ", totalCost)