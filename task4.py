
n = int(input())
employees = []

for _ in range(n):
    data = input().split()

    emp_id = data[0]
    name = data[1]
    basic = float(data[2])
    allowance = float(data[3])
    overtime = float(data[4])
    incentive = float(data[5])

    # Validate salary inputs
    if min(basic, allowance, overtime, incentive) < 0:
        print(emp_id, "Invalid salary details")
        continue

    gross = basic + allowance + overtime + incentive

    # Progressive deductions
    if gross <= 20000:
        deduction = gross * 0.05
    elif gross <= 50000:
        deduction = 20000 * 0.05 + (gross - 20000) * 0.10
    else:
        deduction = (20000 * 0.05
                     + 30000 * 0.10
                     + (gross - 50000) * 0.15)

    net_salary = gross - deduction

    employees.append(
        (emp_id, name, basic, allowance, overtime,
         incentive, gross, deduction, net_salary)
    )

print("\n" + "=" * 85)
print("                 EMPLOYEE SALARY STATEMENT")
print("=" * 85)

print(f"{'ID':<8}{'Name':<12}{'Basic':>10}"
      f"{'Allow.':>10}{'OT':>9}{'Incent.':>10}"
      f"{'Gross':>10}{'Deduct.':>9}{'Net':>10}")

print("-" * 85)

for e in employees:
    print(f"{e[0]:<8}{e[1]:<12}{e[2]:>10.2f}"
          f"{e[3]:>10.2f}{e[4]:>9.2f}{e[5]:>10.2f}"
          f"{e[6]:>10.2f}{e[7]:>9.2f}{e[8]:>10.2f}")

print("=" * 85)
