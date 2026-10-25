
n = int(input())

for _ in range(n):
    data = input().split()

    product = data[0]
    quantity = int(data[1])
    material_cost = float(data[2])
    labour_cost = float(data[3])
    wastage_percent = float(data[4])
    machine_cost = float(data[5])
    selling_price = float(data[6])
    profit_target = float(data[7])

    # Validate inputs
    if (quantity <= 0 or
        min(material_cost, labour_cost, machine_cost,
            selling_price, profit_target) < 0 or
        not 0 <= wastage_percent <= 100):
        print(product, "Invalid input")
        continue

    # Calculate costs
    material_total = quantity * material_cost
    wastage_cost = material_total * wastage_percent / 100
    labour_total = quantity * labour_cost
    machine_total = quantity * machine_cost

    total_cost = (
        material_total + wastage_cost +
        labour_total + machine_total
    )

    revenue = quantity * selling_price
    profit = revenue - total_cost

    profit_percent = (
        profit / total_cost * 100
        if total_cost > 0 else 0
    )

    print("\nProduct:", product)
    print(f"Material Cost: Rs.{material_total:.2f}")
    print(f"Wastage Cost: Rs.{wastage_cost:.2f}")
    print(f"Labour Cost: Rs.{labour_total:.2f}")
    print(f"Machine Cost: Rs.{machine_total:.2f}")
    print(f"Total Cost: Rs.{total_cost:.2f}")
    print(f"Total Revenue: Rs.{revenue:.2f}")
    print(f"Profit/Loss: Rs.{profit:.2f}")
    print(f"Profit Percentage: {profit_percent:.2f}%")

    if profit_percent >= profit_target:
        print("Profit target achieved")
    else:
        print("Profit target not achieved")
