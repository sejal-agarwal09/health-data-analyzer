import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("health_data.csv")

print("Health Data Analyzer")
print()

print("Average BMI:", round(data["BMI"].mean(), 2))
print("Average Sleep:", round(data["Sleep_Hours"].mean(), 2))
print("Average Exercise:", round(data["Exercise_Hours"].mean(), 2))
print("Average Heart Rate:", round(data["Heart_Rate"].mean(), 2))

plt.scatter(data["Sleep_Hours"], data["Heart_Rate"])
plt.xlabel("Sleep (hours)")
plt.ylabel("Heart Rate")
plt.title("Sleep vs. Heart Rate")
plt.show()

plt.scatter(data["Exercise_Hours"], data["BMI"])
plt.xlabel("Exercise (hours)")
plt.ylabel("BMI")
plt.title("Exercise vs. BMI")
plt.show()