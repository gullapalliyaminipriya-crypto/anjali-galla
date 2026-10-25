
n = int(input())
patients = []

for _ in range(n):
    data = input().split()

    patient_id = data[0]
    name = data[1]
    consultation = float(data[2])
    diagnostic = float(data[3])
    treatment = float(data[4])
    age = int(data[5])
    insurance = data[6].lower()

    # Validate billing constraints
    if min(consultation, diagnostic, treatment) < 0 or age < 0:
        print(patient_id, "Invalid billing data")
        continue

    total = consultation + diagnostic + treatment

    # Apply concessions
    concession = 0

    if age >= 60:
        concession += total * 0.10

    if insurance == "yes":
        concession += total * 0.15

    # Maximum concession is 25%
    concession = min(concession, total * 0.25)
    final_bill = total - concession

    # Patient classification
    if insurance == "yes":
        category = "Insured"
    elif final_bill >= 10000:
        category = "High Payment"
    elif final_bill >= 5000:
        category = "Medium Payment"
    else:
        category = "Low Payment"

    patients.append(
        (patient_id, name, total, concession,
         final_bill, category)
    )

print("\nHospital Billing Report")
print("ID Name Total Concession FinalBill Category")

for p in patients:
    print(
        p[0], p[1],
        f"{p[2]:.2f}",
        f"{p[3]:.2f}",
        f"{p[4]:.2f}",
        p[5]
    )
