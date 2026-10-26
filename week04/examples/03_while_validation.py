quantity = int(input("Quantity (positive): "))

while quantity <= 0:
    print("Enter a positive whole number.")
    quantity = int(input("Quantity (positive): "))
print("Accepted:", quantity)
