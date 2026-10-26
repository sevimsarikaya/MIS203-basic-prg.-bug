tax_rate = 0.20

def add_tax(amount):
    tax = amount * tax_rate
    return amount + tax

print(add_tax(100))
# The local variable tax belongs to add_tax.
