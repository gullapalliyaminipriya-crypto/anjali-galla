
n = int(input())
students = []

for _ in range(n):
    data = input().split()

    roll = data[0]
    name = data[1]
    marks = list(map(float, data[2:5]))
    attendance = float(data[5])
    income = float(data[6])

    aggregate = sum(marks) / len(marks)

    if (aggregate >= 75 and
        all(m >= 40 for m in marks) and
        attendance >= 75 and
        income <= 200000):

        students.append({
            "roll": roll,
            "name": name,
            "marks": marks,
            "aggregate": aggregate,
            "attendance": attendance,
            "income": income
        })

# Ranking: aggregate marks, attendance, lower income, roll number
students.sort(
    key=lambda s: (
        -s["aggregate"],
        -s["attendance"],
        s["income"],
        s["roll"]
    )
)

if students:
    print("Eligible Scholarship Candidates:")
    for rank, s in enumerate(students, start=1):
        print(
            rank, s["roll"], s["name"],
            f"{s['aggregate']:.2f}",
            f"{s['attendance']:.2f}",
            f"{s['income']:.2f}"
        )
else:
    print("No eligible candidates")
