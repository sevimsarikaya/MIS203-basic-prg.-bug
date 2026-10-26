"""Week 5 project B: calculate an expense summary with small functions."""

def read_nonnegative(prompt):
    while True:
        try:
            value = float(input(prompt))
        except ValueError:
            print("Please enter a number.")
            continue
        if value >= 0:
            return value
        print("Negative expenses are not accepted.")


def update_total(current_total, new_amount):
    return current_total + new_amount


def update_largest(current_largest, new_amount):
    if current_largest is None or new_amount > current_largest:
        return new_amount
    return current_largest


def is_large(amount, threshold):
    return amount > threshold


def main():
    print("Expense Analyzer")
    count = int(read_nonnegative("How many expenses? "))
    if count == 0:
        print("No expenses to analyze.")
        return
    threshold = read_nonnegative("Large-expense threshold: ")
    total = 0.0
    largest = None
    large_count = 0
    for position in range(1, count + 1):
        amount = read_nonnegative(f"Expense {position}: ")
        total = update_total(total, amount)
        largest = update_largest(largest, amount)
        if is_large(amount, threshold):
            large_count += 1
    print(f"Total expenses: {total:.2f} TRY")
    print(f"Average: {total / count:.2f} TRY")
    print(f"Largest: {largest:.2f} TRY")
    print(f"Above threshold: {large_count}")


if __name__ == "__main__":
    assert update_total(10, 20) == 30
    assert update_largest(20, 30) == 30
    assert is_large(30, 20)
    main()
