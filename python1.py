# Smart Shopping Cart Calculator
# Electronics Store

# Customer information

print("SMART SHOPPING CART")

name = input("Enter your name: ")

member_answer = input("Are you a member? (yes/no): ")
is_member = member_answer == "yes"

previous_purchases = float(input("Enter previous purchases: "))


# Enter 3 items

print("\nEnter item 1 information")

item1 = input("Item name: ")
price1 = float(input("Item price: "))
quantity1 = int(input("Quantity: "))

print("\nEnter item 2 information")

item2 = input("Item name: ")
price2 = float(input("Item price: "))
quantity2 = int(input("Quantity: "))

print("\nEnter item 3 information")

item3 = input("Item name: ")
price3 = float(input("Item price: "))
quantity3 = int(input("Quantity: "))


# Calculate item totals

total1 = price1 * quantity1
total2 = price2 * quantity2
total3 = price3 * quantity3

total_items = quantity1 + quantity2 + quantity3

subtotal = total1 + total2 + total3


# Check discount eligibility

member_eligible = is_member
bulk_eligible = total_items > 5
loyalty_eligible = previous_purchases >= 1000000


# Calculate discounts

member_discount = member_eligible * 0.10 * subtotal

price_after_member = subtotal - member_discount

bulk_discount = bulk_eligible * 0.05 * price_after_member

price_after_bulk = price_after_member - bulk_discount

loyalty_discount = loyalty_eligible * 0.03 * price_after_bulk

final_subtotal = price_after_bulk - loyalty_discount

total_discount = member_discount + bulk_discount + loyalty_discount


# Calculate tax

tax = final_subtotal * 0.12


# Calculate shipping

free_shipping = subtotal > 500000

shipping = (subtotal <= 500000) * 25000


# Calculate final price

final_price = final_subtotal + tax + shipping


# Print receipt

print("\n")
print("========== RECEIPT ==========")

print("Customer:", name)
print("Member:", is_member)
print("Previous purchases:", previous_purchases)

print("\n--- ITEMS ---")

print(item1, quantity1, "x", price1, "=", total1)
print(item2, quantity2, "x", price2, "=", total2)
print(item3, quantity3, "x", price3, "=", total3)

print("\nTotal items:", total_items)
print("Subtotal:", subtotal)

print("\n--- DISCOUNTS ---")

print("Member eligible:", member_eligible)
print("Member discount:", member_discount)

print("Bulk eligible:", bulk_eligible)
print("Bulk discount:", bulk_discount)

print("Loyalty eligible:", loyalty_eligible)
print("Loyalty discount:", loyalty_discount)

print("Total discount:", total_discount)
print("Subtotal after discounts:", final_subtotal)

print("\n--- TAX AND SHIPPING ---")

print("Tax:", tax)
print("Free shipping:", free_shipping)
print("Shipping cost:", shipping)

print("\n--- FINAL RESULT ---")

print("Final price:", final_price)
print("Total amount saved:", total_discount)

print("=============================")