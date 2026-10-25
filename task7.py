
n = int(input())
items = []

subtotal = 0
total_tax = 0

for _ in range(n):
    data = input().split()

    name = data[0]
    category = data[1].lower()
    price = float(data[2])
    quantity = int(data[3])

    if price < 0 or quantity <= 0:
        print("Invalid product details:", name)
        continue

    amount = price * quantity

    # Category-specific tax rates
    if category == "food":
        tax_rate = 5
    elif category == "clothing":
        tax_rate = 5
    elif category == "electronics":
        tax_rate = 18
    else:
        tax_rate = 12

    tax = amount * tax_rate / 100

    subtotal += amount
    total_tax += tax

    items.append(
        (name, category, price, quantity, amount, tax, tax_rate)
    )

# Threshold-based discounts
if subtotal >= 10000:
    discount_rate = 15
elif subtotal >= 5000:
    discount_rate = 10
elif subtotal >= 2000:
    discount_rate = 5
else:
    discount_rate = 0

discount = subtotal * discount_rate / 100

# Maximum concession limit
max_discount = subtotal * 0.15
discount = min(discount, max_discount)

final_amount = subtotal - discount + total_tax

print("\n" + "=" * 78)
print("                         RETAIL INVOICE")
print("=" * 78)
print(f"{'Product':<15}{'Category':<15}{'Price':>9}"
      f"{'Qty':>5}{'Amount':>10}{'Tax':>10}")
print("-" * 78)

for item in items:
    print(f"{item[0]:<15}{item[1]:<15}{item[2]:>9.2f}"
          f"{item[3]:>5}{item[4]:>10.2f}{item[5]:>10.2f}")

print("-" * 78)
print(f"Subtotal:              Rs.{subtotal:.2f}")
print(f"Discount ({discount_rate}%):        Rs.{discount:.2f}")
print(f"Total Tax:             Rs.{total_tax:.2f}")
print(f"Final Amount:          Rs.{final_amount:.2f}")
print("=" * 78)
