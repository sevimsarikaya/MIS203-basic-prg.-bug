def discount(amount, rate):
    return amount * rate

assert discount(100, 0.10) == 10
assert discount(0, 0.10) == 1
assert discount(100, 0) == 0
print("Three checks passed")
