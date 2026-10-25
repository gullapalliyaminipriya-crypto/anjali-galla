
n = int(input())

data_used = float(input())
call_minutes = int(input())
required_validity = int(input())
budget = float(input())

plans = []

for _ in range(n):
    details = input().split()

    name = details[0]
    price = float(details[1])
    data_limit = float(details[2])
    call_limit = int(details[3])
    validity = int(details[4])
    extra_data_rate = float(details[5])
    extra_call_rate = float(details[6])

    # Calculate excess charges
    excess_data = max(0, data_used - data_limit)
    excess_calls = max(0, call_minutes - call_limit)

    extra_charge = (
        excess_data * extra_data_rate
        + excess_calls * extra_call_rate
    )

    total_cost = price + extra_charge

    # Check validity and budget
    if validity >= required_validity and total_cost <= budget:
        plans.append(
            (name, price, extra_charge, total_cost, validity)
        )

# Sort by total cost, then longer validity, then plan name
plans.sort(key=lambda p: (p[3], -p[4], p[0]))

print("\nPlan Comparison")

if plans:
    for p in plans:
        print(
            p[0],
            f"Base: Rs.{p[1]:.2f}",
            f"Excess: Rs.{p[2]:.2f}",
            f"Total: Rs.{p[3]:.2f}"
        )

    best = plans[0]
    print("\nMost Economical Eligible Plan:", best[0])
    print(f"Total Cost: Rs.{best[3]:.2f}")
else:
    print("No eligible plan available")
