
print("=== Arcade Game Center Calculator ===")
print("Enter game type: classic, modern, or premium")
print("Type 'done' when finished playing")

total = 0

while True:
    game = input("\nEnter game type: ")

    if game == "done":
        break

    elif game == "classic":
        price = 0.50

    elif game == "modern":
        price = 1.50

    elif game == "premium":
        price = 2.50

    else:
        print("Invalid game type")
        continue

    total = total + price

    print(f"Price: ${price:.2f}")
    print(f"Current total: ${total:.2f}")

print("\n=== Game Summary ===")
print(f"Subtotal: ${total:.2f}")

if total >= 10.00:
    bonus = 1.50
else:
    bonus = 0.00

final_total = total - bonus

print(f"Token Bonus Credit: -${bonus:.2f}")
print(f"Final Total: ${final_total:.2f}")

print("Thank you for playing!")
