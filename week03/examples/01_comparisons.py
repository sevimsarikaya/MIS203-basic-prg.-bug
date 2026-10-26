amount = float(input("Order amount: "))

print("Over free-delivery threshold:", amount >= 500)
print("Exactly at threshold:", amount == 500)
print("Below threshold:", amount < 500)
print("Not below threshold:", amount >= 500)

x = 10
y = 10
print("x is less than y:", x < y)
print("x is greater than y:", x > y)


def is_even(n):
    """_summary_

    Args:"
        n (_type_): _description_

    Returns:
        _type_: _description_
    """
    return n % 2 == 0


print("x is even:", is_even(x))
print("y is even:", is_even(y))

is_even(10)