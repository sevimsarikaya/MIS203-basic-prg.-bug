"""Week 5 project A: a reusable pricing engine with boundary checks."""

def nonnegative_number(prompt):
    while True:
        text = input(prompt).strip()
        try:
            value = float(text)
        except ValueError:
            print("Enter a number.")
            continue
        if value < 0:
            print("Enter zero or more.")
            continue
        return value


def subtotal(quantity, unit_price):
    return quantity * unit_price


def discount_rate(subtotal_amount, member):
    if member and subtotal_amount >= 1000:
        return 0.15
    if member:
        return 0.05
    if subtotal_amount >= 1500:
        return 0.10
    return 0.0


def shipping_fee(amount_after_discount):
    return 0.0 if amount_after_discount >= 500 else 40.0


def quote(quantity, unit_price, member):
    before_discount = subtotal(quantity, unit_price)
    rate = discount_rate(before_discount, member)
    discount = before_discount * rate
    after_discount = before_discount - discount
    shipping = shipping_fee(after_discount)
    return before_discount, rate, discount, shipping, after_discount + shipping


def main():
    print("Reusable Pricing Engine")
    customer = input("Customer: ").strip()
    quantity = nonnegative_number("Quantity: ")
    price = nonnegative_number("Unit price: ")
    member = input("Member (yes/no): ").strip().lower() == "yes"
    before, rate, reduction, shipping, total = quote(quantity, price, member)
    print(f"Quote for {customer}")
    print(f"Subtotal: {before:.2f} TRY")
    print(f"Discount ({rate:.0%}): {reduction:.2f} TRY")
    print(f"Shipping: {shipping:.2f} TRY")
    print(f"Total: {total:.2f} TRY")


if __name__ == "__main__":
    assert quote(1, 100, False)[-1] == 140
    assert quote(10, 100, True)[-1] == 850
    main()
