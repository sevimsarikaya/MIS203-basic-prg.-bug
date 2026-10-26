age = int(input("Age: "))
has_id = input("Has ID (yes/no): ").strip().lower() == "yes"

if age >= 18 and has_id:
    print("Entry permitted")
else:
    print("Entry denied")
# Try age 17 and 18, with and without an ID.
