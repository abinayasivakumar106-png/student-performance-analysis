import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/student_performance_final.csv")

# Display data
print("Student Performance Dataset")
print(df)

# Department-wise average
department_avg = df.groupby("Department")["Average"].mean()

print("\nDepartment-wise Average:")
print(department_avg)

# Plot
department_avg.plot(kind="bar")

plt.title("Department-wise Average Score")
plt.xlabel("Department")
plt.ylabel("Average Score")
plt.tight_layout()
plt.show()
