import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("health_data.csv")

def show_dataset_info():
    print()
    print("Dataset Information")
    print("Number of records:", len(data))
    print("Number of variables:", len(data.columns))

    print()
    print("Variables:")
    for column in data.columns:
        print("-", column)

    print()
    print("Missing values:")
    print(data.isnull().sum())

def show_averages():
    print()
    print("BMI")
    print("  Average:", round(data["BMI"].mean(), 2))
    print("  Minimum:", round(data["BMI"].min(), 2))
    print("  Maximum:", round(data["BMI"].max(), 2))
    print("  Median:", round(data["BMI"].median(), 2))

    print()
    print("Sleep")
    print("  Average:", round(data["Sleep_Hours"].mean(), 2))
    print("  Minimum:", round(data["Sleep_Hours"].min(), 2))
    print("  Maximum:", round(data["Sleep_Hours"].max(), 2))
    print("  Median:", round(data["Sleep_Hours"].median(), 2))

    print()
    print("Exercise")
    print("  Average:", round(data["Exercise_Hours"].mean(), 2))
    print("  Minimum:", round(data["Exercise_Hours"].min(), 2))
    print("  Maximum:", round(data["Exercise_Hours"].max(), 2))
    print("  Median:", round(data["Exercise_Hours"].median(), 2))

    print()
    print("Heart Rate")
    print("  Average:", round(data["Heart_Rate"].mean(), 2))
    print("  Minimum:", round(data["Heart_Rate"].min(), 2))
    print("  Maximum:", round(data["Heart_Rate"].max(), 2))
    print("  Median:", round(data["Heart_Rate"].median(), 2))


def show_sleep_graph():
    plt.scatter(data["Sleep_Hours"], data["Heart_Rate"])
    plt.xlabel("Sleep (hours)")
    plt.ylabel("Heart Rate")
    plt.title("Sleep vs. Heart Rate")
    plt.show()


def show_exercise_graph():
    plt.scatter(data["Exercise_Hours"], data["BMI"])
    plt.xlabel("Exercise (hours)")
    plt.ylabel("BMI")
    plt.title("Exercise vs. BMI")
    plt.show()


def show_correlations():
    print()
    print("Correlations:")
    print("Sleep vs. Heart Rate:",
          round(data["Sleep_Hours"].corr(data["Heart_Rate"]), 2))
    print("Exercise vs. BMI:",
          round(data["Exercise_Hours"].corr(data["BMI"]), 2))


print("Health Data Analyzer")

while True:
    print()
    print("1. View summary statistics")
    print("2. View dataset information")
    print("3. View sleep and heart rate graph")
    print("4. View exercise and BMI graph")
    print("5. View correlations")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        show_averages()
    elif choice == "2":
        show_dataset_info()
    elif choice == "3":
        show_sleep_graph()
    elif choice == "4":
        show_exercise_graph()
    elif choice == "5":
        show_correlations()
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Please choose a number from 1 to 6.")