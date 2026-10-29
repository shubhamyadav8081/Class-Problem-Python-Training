
import pandas as pd
import matplotlib.pyplot as plt

# ==========================================
# STEP 1: STUDENT NAMES
# ==========================================

names = [
    "AARUSHI AGARWAL", "AARYAN VERMA", "AASHUTOSH JOSHI",
    "ABHAV CHAUHAN", "ABHISHEK GUPTA", "ADITYA VARDHAN",
    "AMAN KUMAR", "ANANT DAGAR", "ANANYA SRIVASTAVA",
    "ANKIT SINGH", "ANSHUL YADAV", "ANUBHAV TYAGI",
    "ANUJ SHUKLA", "ANURAG TRIPATHI", "ARYAN GUPTA",
    "ASHISH SONI", "ASHU KUMAR THAKUR", "ASHUTOSH PATRO",
    "ASTHA MISHRA", "BHOOMI JAISWAL", "BITU SHARMA",
    "DEEPAK SHARMA", "DEVESH GUPTA", "DIPANSHU PAL",
    "DIVYANSH DIGARI", "DUSHIENTH RANA", "GAURAV YADAV",
    "HARSHIT MEHTA", "HARSHITA SINGH", "HIMANSHU SAW",
    "ISHA KUMARI", "KHARANSHU GUPTA", "KRITIKA SHIVHARE",
    "LAVI YADAV", "MAHIMA PATEL", "MANISH KUMAR YADAV",
    "MANYA CHAHAL", "MOHD ARQAM", "MOHD IKAN",
    "MOKSHIT TYAGI", "NEHA", "NIKHIL KUSHWAHA",
    "PRERNA JAIN", "PRIYANK DEVAL", "PRIYANSHI PANDEY",
    "PRIYANSHU KUMAR", "RAJAT PATEL", "RAJDEEP NIRANJAN",
    "RIDHI JAIN", "RIMJHIM SHARMA", "RISHI RANJAN KUMAR",
    "SAMEER SINGH", "SANDEEP SHARMA", "SHIVANSH MISHRA",
    "SHREYA KUMARI", "SHRIRAM SAINI", "SHUBHAM GIRI",
    "SHUBHAM YADAV", "SHUBHI SINGH", "SIDDHARTH",
    "SOMYA", "SONU KUMAR", "SUJAL TOMAR", "TANMAY",
    "UNNATI CHAUDHARY", "UTKARSH SINGH", "VANSH RAJ SINGH",
    "VANSHIKA", "VANSHIKA", "VEDANT CHAUDHARY",
    "VIKRAM MAURYA", "YASH PARASHAR", "YASHI APANSHI",
    "YOGESH TIWARI", "YUG GARG", "AMAAN RAZA",
    "SWATI KUMARI"
]

# ==========================================
# STEP 2: SAMPLE STUDENT DATA
# ==========================================

departments = ["CSE", "IT", "ECE", "EE"]

skills = [
    "Python, SQL",
    "C++, DSA",
    "HTML, CSS, JavaScript",
    "Python, Excel",
    "Java, SQL"
]

n = len(names)

df = pd.DataFrame({
    "Name": names,
    "Age": [18 + (i % 5) for i in range(n)],
    "Performance": [55 + ((i * 7) % 46) for i in range(n)],
    "Department": [departments[i % 4] for i in range(n)],
    "Job_Selection": [
        "Yes" if i % 3 == 0 else "No" for i in range(n)
    ],
    "Skills": [skills[i % len(skills)] for i in range(n)]
})

# ==========================================
# STEP 3: SHUBHAM YADAV AS ECE TOP PERFORMER
# ==========================================

df.loc[
    df["Name"] == "SHUBHAM YADAV", "Department"
] = "ECE"

df.loc[
    df["Name"] == "SHUBHAM YADAV", "Performance"
] = 94
df.loc[
    df["Name"] == "Arayan Verma", "Department"
] = "ECE"

df.loc[
    df["Name"] == "Arayan Verma ", "Performance"
] = 94

# ==========================================
# STEP 4: CALCULATE ANNUAL PACKAGE
# Example package values in LPA
# ==========================================

def calculate_package(performance):
    if performance >= 90:
        return 12.0
    elif performance >= 75:
        return 8.0
    elif performance >= 60:
        return 5.0
    else:
        return 3.0

df["Annual_Package_LPA"] = df["Performance"].apply(
    calculate_package
)

# ==========================================
# STEP 5: PERFORMANCE CATEGORY
# ==========================================

def get_category(performance):
    if performance >= 75:
        return "Top"
    elif performance >= 60:
        return "Average"
    else:
        return "Below Average"

df["Performance_Category"] = df["Performance"].apply(
    get_category
)

# ==========================================
# STEP 6: DISPLAY STUDENT DATA
# ==========================================

print("\n========== COMPLETE STUDENT DATA ==========")
print(df.to_string(index=False))

# ==========================================
# STEP 7: IT DEPARTMENT STUDENTS
# ==========================================

print("\n========== IT DEPARTMENT STUDENTS ==========")
print(
    df.loc[df["Department"] == "IT", ["Name", "Age"]]
    .to_string(index=False)
)

# ==========================================
# STEP 8: ECE DEPARTMENT STUDENTS
# ==========================================

print("\n========== ECE DEPARTMENT STUDENTS ==========")
print(
    df.loc[df["Department"] == "ECE", ["Name", "Age"]]
    .to_string(index=False)
)

# ==========================================
# STEP 9: DEPARTMENT-WISE STUDENT COUNT
# ==========================================

print("\n========== DEPARTMENT-WISE STUDENT COUNT ==========")
print(df["Department"].value_counts())

# ==========================================
# STEP 10: AVERAGE PACKAGE BY DEPARTMENT
# ==========================================

print("\n========== AVERAGE PACKAGE ==========")
print(
    df.groupby("Department")["Annual_Package_LPA"]
    .mean().round(2)
)

# ==========================================
# STEP 11: TOP PERFORMER OF EACH DEPARTMENT
# ==========================================

print("\n========== TOP PERFORMER ==========")

top_indices = df.groupby("Department")["Performance"].idxmax()

top_students = df.loc[
    top_indices,
    ["Name", "Department", "Performance"]
]

print(top_students.to_string(index=False))

# ==========================================
# STEP 12: AVERAGE PERFORMANCE BY DEPARTMENT
# ==========================================

print("\n========== AVERAGE PERFORMANCE ==========")
print(
    df.groupby("Department")["Performance"]
    .mean().round(2)
)

# ==========================================
# STEP 13: LOWEST PERFORMER OF EACH DEPARTMENT
# ==========================================

print("\n========== LOWEST PERFORMER ==========")

low_indices = df.groupby("Department")["Performance"].idxmin()

print(
    df.loc[
        low_indices,
        ["Name", "Department", "Performance"]
    ].to_string(index=False)
)

# ==========================================
# STEP 14: JOB SELECTION COUNT
# ==========================================

print("\n========== JOB SELECTION COUNT ==========")
print(df["Job_Selection"].value_counts())

# ==========================================
# STEP 15: HIGHEST, AVERAGE AND LOWEST PACKAGE
# ==========================================

print("\n========== PACKAGE ANALYSIS ==========")

package_analysis = df.groupby("Department")[
    "Annual_Package_LPA"
].agg(
    Highest="max",
    Average="mean",
    Lowest="min"
)

print(package_analysis.round(2))

# ==========================================
# STEP 16: LINE GRAPH
# TOP, AVERAGE AND BELOW-AVERAGE PERFORMANCE
# ==========================================

top_performance = df.groupby("Department")[
    "Performance"
].max()

average_performance = df.groupby("Department")[
    "Performance"
].mean()

# Average se neeche perform karne wale students ka average
department_average = df.groupby("Department")[
    "Performance"
].transform("mean")

below_average = df[
    df["Performance"] < department_average
].groupby("Department")["Performance"].mean()

department_order = ["CSE", "IT", "ECE", "EE"]

top_performance = top_performance.reindex(department_order)
average_performance = average_performance.reindex(department_order)
below_average = below_average.reindex(department_order)

fig, ax = plt.subplots(figsize=(11, 6))

ax.plot(
    department_order,
    top_performance,
    marker="o",
    linewidth=2.5,
    label="Top Performer"
)

ax.plot(
    department_order,
    average_performance,
    marker="s",
    linewidth=2.5,
    label="Average Performance"
)

ax.plot(
    department_order,
    below_average,
    marker="^",
    linewidth=2.5,
    label="Below-Average Students' Average"
)

# ECE mein Shubham Yadav ka top performance label
ece_position = department_order.index("ECE")

ax.annotate(
    "SHUBHAM YADAV (100)",
    xy=("ECE", 100),
    xytext=(10, -20),
    textcoords="offset points",
    arrowprops=dict(arrowstyle="->"),
    fontsize=10,
    fontweight="bold"
)

ax.set_title(
    "Department-wise Student Performance",
    fontsize=14,
    fontweight="bold"
)

ax.set_xlabel("Department / Branch")
ax.set_ylabel("Performance Score")
ax.set_ylim(0, 110)
ax.legend()
ax.grid(True, linestyle="--", alpha=0.5)

plt.tight_layout()
plt.savefig("student_performance_graph.png", dpi=150)
plt.show()

# ==========================================
# STEP 17: DEPARTMENT-WISE STUDENT COUNT GRAPH
# ==========================================

df["Department"].value_counts().reindex(
    department_order, fill_value=0
).plot(
    kind="bar",
    figsize=(8, 5),
    color="skyblue",
    edgecolor="black"
)

plt.title("Department-wise Student Count")
plt.xlabel("Department")
plt.ylabel("Number of Students")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("department_count.png", dpi=150)
plt.show()

# ==========================================
# STEP 18: SAVE DATA TO CSV
# ==========================================

df.to_csv("student_analysis_output.csv", index=False)

print("\nAnalysis completed successfully!")
print("CSV saved: student_analysis_output.csv")
print("Graphs saved:")
print("1. student_performance_graph.png")
print("2. department_count.png")
