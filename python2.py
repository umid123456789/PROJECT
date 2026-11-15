
print("=== Pet Grooming Service Calculator ===")
print("Enter service package: bath, trim, or full")
print("Type 'done' when finished selecting services")

total = 0

while True:
    service = input("\nEnter service package: ")

    if service == "done":
        break

    elif service == "bath":
        price = 15.00

    elif service == "trim":
        price = 25.00

    elif service == "full":
        price = 40.00

    else:
        print("Invalid service package")
        continue

    total = total + price

    print(f"Price: ${price:.2f}")
    print(f"Current total: ${total:.2f}")

print("\n=== Service Summary ===")
print(f"Subtotal: ${total:.2f}")

if total >= 75.00:
    discount = 12.00
else:
    discount = 0.00

final_total = total - discount

print(f"Multi-Pet Discount: -${discount:.2f}")
print(f"Final Total: ${final_total:.2f}")

print("Thank you for choosing our salon!")   
