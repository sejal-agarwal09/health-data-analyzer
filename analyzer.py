import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("health_data.csv")


def show_averages():
    print()
    print("Average BMI:", round(data["BMI"].mean(), 2))
    print("Average Sleep:", round(data["Sleep_Hours"].mean(), 2))
    print("Average Exercise:", round(data["Exercise_Hours"].mean(), 2))
    print("Average Heart Rate:", round(data["Heart_Rate"].mean(), 2))


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
    print("1. View average statistics")
    print("2. View sleep and heart rate graph")
    print("3. View exercise and BMI graph")
    print("4. View correlations")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        show_averages()
    elif choice == "2":
        show_sleep_graph()
    elif choice == "3":
        show_exercise_graph()
    elif choice == "4":
        show_correlations()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Please choose a number from 1 to 5.")