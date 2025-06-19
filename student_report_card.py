# 🧾 Student Report Card Generator (Version 2)

# 🎤 Input
name = input("Enter Your Name: ")
marks1 = int(input("Enter Marks For Math: "))
marks2 = int(input("Enter Marks For Science: "))
marks3 = int(input("Enter Marks For English: "))

# 🧮 Total, Average, Percentage
total = marks1 + marks2 + marks3
avg = total / 3
percentage = (total / 300) * 100

# 📋 Subject-wise Pass/Fail Check
subject_results = []
for subject, mark in [("Math", marks1), ("Science", marks2), ("English", marks3)]:
    status = "✅ Pass" if mark >= 33 else "❌ Fail"
    subject_results.append((subject, mark, status))

# 🎯 Grade Calculation
if marks1 < 33 or marks2 < 33 or marks3 < 33:
    grade = "F"
    result = "❌ Fail (One or more subjects below 33)"
else:
    if avg >= 90:
        grade = "A+"
    elif avg >= 80:
        grade = "A"
    elif avg >= 70:
        grade = "B"
    elif avg >= 60:
        grade = "C"
    elif avg >= 50:
        grade = "D"
    else:
        grade = "E"
    result = "✅ Pass"

# 📄 Final Report
print("\n📄 STUDENT REPORT CARD")
print("----------------------------")
print("Name:", name)
for subject, mark, status in subject_results:
    print(f"{subject}: {mark} -> {status}")
print("----------------------------")
print("Total Marks:", total, "/ 300")
print("Average:", round(avg, 2))
print("Percentage:", round(percentage, 2), "%")
print("Grade:", grade)
print("Result:", result)
