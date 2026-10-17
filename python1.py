
# Electronics Store

# Input information for 3 items 
item_name1 = input('Item name 1: ')
price1 = float(input('Price 1: '))
quantity1 = int(input('Quantity 1: '))

item_name2 = input('Item name 2: ')
price2 = float(input('Price 2: '))
quantity2 = int(input('Quantity 2: '))

item_name3 = input('Item name 3: ')
price3 = float(input('Price 3: '))
quantity3 = int(input('Quantity 3: '))

# Customer information 
name = input('Write your name: ')
is_member = input('Membership (yes/no): ')
total_previous_purchase = float(input('Total previous purchase: '))

# Calculate subtotal
total1 = price1 * quantity1
total2 = price2 * quantity2
total3 = price3 * quantity3

subtotal_before_discounts = total1 + total2 + total3
subtotal = subtotal_before_discounts

# Member discount 
member_eligible = is_member == 'yes'
member_discount = member_eligible * 0.10 * subtotal
subtotal = subtotal - member_discount

# Bulk discount
total_items = quantity1 + quantity2 + quantity3
bulk_eligible = total_items > 5
bulk_discount = bulk_eligible * 0.05 * subtotal
subtotal = subtotal - bulk_discount

# Loyalty discount
loyalty_eligible = total_previous_purchase >= 1000000
loyalty_discount = loyalty_eligible * 0.03 * subtotal
subtotal = subtotal - loyalty_discount

# Total discount 
total_discount = member_discount + bulk_discount + loyalty_discount
after_discounts = subtotal

# Tax 
tax = after_discounts * 0.12
subtotal = subtotal + tax

# Shipping 
shipping = (subtotal_before_discounts <= 500000) * 25000
subtotal = subtotal + shipping

# Final total
final_total = subtotal

# Output
print()
print('Customer name:', name)
print('Membership status:', is_member)

print()
print('Item:', item_name1, 'Quantity:', quantity1, 'Price:', price1, 'Total:', total1)
print('Item:', item_name2, 'Quantity:', quantity2, 'Price:', price2, 'Total:', total2)
print('Item:', item_name3, 'Quantity:', quantity3, 'Price:', price3, 'Total:', total3)

print()
print('Subtotal before discounts:', subtotal_before_discounts)

print('Member discount eligibility:', member_eligible)
print('Member discount amount:', member_discount)

print('Bulk discount eligibility:', bulk_eligible)
print('Bulk discount amount:', bulk_discount)

print('Loyalty discount eligibility:', loyalty_eligible)
print('Loyalty discount amount:', loyalty_discount)

print('Total discounts:', total_discount)
print('Subtotal after discounts:', after_discounts)

print('Tax amount:', tax)

print('Free shipping status:', subtotal_before_discounts > 500000)
print('Shipping cost:', shipping)

print('Final total:', final_total)
print('Total amount saved:', total_discount)


