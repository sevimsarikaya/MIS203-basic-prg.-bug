def final_price(subtotal, discount_rate=0.0):
    return subtotal * (1 - discount_rate)

print(final_price(500))
print(final_price(500, 0.10))
