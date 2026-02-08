item_cost = float(input("Enter the cost of the item: "))
tax_rate = float(input("Enter the tax rate (as a percentage): "))

# Calculate the total cost including tax
total_cost = item_cost + (item_cost * tax_rate / 100)

print(f"The total cost of the item including tax is: {total_cost}")