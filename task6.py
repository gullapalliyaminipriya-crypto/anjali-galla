
n = int(input())
passengers = []

for _ in range(n):
    data = input().split()

    name = data[0]
    distance = float(data[1])
    travel_class = data[2].upper()
    age = int(data[3])
    cancelled = data[4].lower()

    # Validate input
    if distance <= 0 or age < 0:
        print(name, "Invalid passenger details")
        continue

    # Distance-based fare per km
    if distance <= 100:
        rate = 1.00
    elif distance <= 500:
        rate = 1.50
    else:
        rate = 2.00

    # Travel class multiplier
    class_rates = {
        "SLEEPER": 1.0,
        "AC3": 2.0,
        "AC2": 3.0,
        "AC1": 4.0
    }

    if travel_class not in class_rates:
        print(name, "Invalid travel class")
        continue

    basic_fare = distance * rate * class_rates[travel_class]

    # Age-based concession
    concession = 0

    if age < 5:
        concession = basic_fare
    elif age >= 60:
        concession = basic_fare * 0.40

    fare_after_concession = basic_fare - concession

    # Reservation fee
    reservation_fee = 50 if travel_class != "SLEEPER" else 20

    total_fare = fare_after_concession + reservation_fee

    # Cancellation penalty
    if cancelled == "yes":
        cancellation_penalty = total_fare * 0.25
        refund = total_fare - cancellation_penalty
    else:
        cancellation_penalty = 0
        refund = 0

    passengers.append((
        name, basic_fare, concession, reservation_fee,
        total_fare, cancellation_penalty, refund, cancelled
    ))

print("\nRAILWAY FARE STATEMENT")
print("-" * 100)
print(f"{'Name':<12}{'Basic':>10}{'Concession':>12}"
      f"{'Reserve':>10}{'Fare':>10}{'Penalty':>10}{'Refund':>10}")
print("-" * 100)

for p in passengers:
    print(f"{p[0]:<12}{p[1]:>10.2f}{p[2]:>12.2f}"
          f"{p[3]:>10.2f}{p[4]:>10.2f}{p[5]:>10.2f}{p[6]:>10.2f}")

print("-" * 100)
