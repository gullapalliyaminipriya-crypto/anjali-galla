
n = int(input())

budget = float(input())
fee_percent = float(input())

expenses = []
total_spending = 0

for _ in range(n):
    data = input().split()

    category = data[0]
    amount = float(data[1])
    exchange_rate = float(data[2])

    if amount < 0 or exchange_rate <= 0:
        print(category, "Invalid input")
        continue

    converted_amount = amount * exchange_rate
    conversion_fee = converted_amount * fee_percent / 100
    final_amount = converted_amount + conversion_fee

    expenses.append(
        (category, converted_amount, conversion_fee, final_amount)
    )

    total_spending += final_amount

print("\nTRAVEL BUDGET REPORT")
print("-" * 65)
print(f"{'Category':<15}{'Converted':>15}"
      f"{'Fee':>12}{'Total':>15}")
print("-" * 65)

for e in expenses:
    print(f"{e[0]:<15}{e[1]:>15.2f}"
          f"{e[2]:>12.2f}{e[3]:>15.2f}")

print("-" * 65)
print(f"Total Spending: Rs.{total_spending:.2f}")
print(f"Travel Budget:  Rs.{budget:.2f}")

difference = budget - total_spending

if difference >= 0:
    print(f"Remaining Budget: Rs.{difference:.2f}")
else:
    print(f"Budget Exceeded: Rs.{abs(difference):.2f}")

if expenses:
    largest = max(expenses, key=lambda e: e[3])
    print("Largest Expense Category:", largest[0])
    print(f"Largest Expense: Rs.{largest[3]:.2f}")
else:
    print("No valid expenses recorded")
