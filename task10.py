
# Campus Event Financial Planning

venue = float(input())
equipment = float(input())
catering_per_person = float(input())
transport_per_person = float(input())
certificate_per_person = float(input())

participants = int(input())
registration_fee = float(input())
sponsorship = float(input())

# Validate inputs
if (min(venue, equipment, catering_per_person,
        transport_per_person, certificate_per_person,
        registration_fee, sponsorship) < 0
        or participants < 0):
    print("Invalid input")

else:
    # Calculate costs
    fixed_cost = venue + equipment
    variable_cost = (
        catering_per_person
        + transport_per_person
        + certificate_per_person
    )

    total_variable_cost = variable_cost * participants
    total_cost = fixed_cost + total_variable_cost

    participant_contributions = participants * registration_fee
    total_funds = participant_contributions + sponsorship

    balance = total_funds - total_cost

    # Sponsorship shortfall before registration income
    sponsorship_shortfall = max(0, total_cost - sponsorship)

    # Minimum registrations needed to break even
    if registration_fee > variable_cost:
        required = max(
            0,
            int((fixed_cost - sponsorship) /
                (registration_fee - variable_cost)) + 1
        )

        # Correct rounding for exact break-even cases
        while (required > 0 and
               sponsorship + (required - 1) * registration_fee
               >= fixed_cost + (required - 1) * variable_cost):
            required -= 1
    elif sponsorship >= fixed_cost:
        required = 0
    else:
        required = -1

    print("\nCAMPUS EVENT FINANCIAL REPORT")
    print("-" * 40)
    print(f"Venue Cost: Rs.{venue:.2f}")
    print(f"Equipment Cost: Rs.{equipment:.2f}")
    print(f"Fixed Cost: Rs.{fixed_cost:.2f}")
    print(f"Variable Cost per Participant: Rs.{variable_cost:.2f}")
    print(f"Total Variable Cost: Rs.{total_variable_cost:.2f}")
    print(f"Total Event Cost: Rs.{total_cost:.2f}")
    print(f"Participant Contributions: Rs.{participant_contributions:.2f}")
    print(f"Sponsorship: Rs.{sponsorship:.2f}")
    print(f"Sponsorship Shortfall: Rs.{sponsorship_shortfall:.2f}")
    print(f"Final Balance: Rs.{balance:.2f}")

    if required == -1:
        print("Break-even is not possible at this registration fee.")
    else:
        print("Minimum Registrations to Break Even:", required)

    if balance >= 0:
        print("Status: Event is financially feasible")
    else:
        print("Status: Additional funds are required")
