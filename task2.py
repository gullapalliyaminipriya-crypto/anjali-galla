
n = int(input())
bills = []

for i in range(n):
    month = input()
    units = float(input())

    # Progressive consumption slabs
    if units <= 100:
        energy_charge = units * 1.50
    elif units <= 200:
        energy_charge = 100 * 1.50 + (units - 100) * 2.50
    elif units <= 300:
        energy_charge = (100 * 1.50 + 100 * 2.50
                         + (units - 200) * 4.00)
    else:
        energy_charge = (100 * 1.50 + 100 * 2.50
                         + 100 * 4.00 + (units - 300) * 6.00)

    fixed_charge = 100
    surcharge = energy_charge * 0.05

    # Rebate for low consumption
    rebate = 50 if units <= 100 else 0

    total = energy_charge + fixed_charge + surcharge - rebate
    total = max(0, total)

    bills.append((month, units, total))

print("\nMonthly Electricity Bills")
print("Month\tUnits\tBill")

for month, units, total in bills:
    print(f"{month}\t{units:.0f}\t{total:.2f}")

print("\nBill Comparison")

for i in range(1, n):
    previous = bills[i - 1][2]
    current = bills[i][2]

    increase = current - previous

    if previous > 0:
        percentage = (increase / previous) * 100
    else:
        percentage = 0

    print(f"{bills[i][0]}: Change = Rs.{increase:.2f}")

    if percentage > 30:
        print("Unusual increase detected!")
