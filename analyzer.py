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

def validate_data():
    print()
    print("Data Validation")

    expected_columns = [
        "Age",
        "BMI",
        "Sleep_Hours",
        "Exercise_Hours",
        "Heart_Rate"
    ]

    missing_columns = []

    for column in expected_columns:
        if column not in data.columns:
            missing_columns.append(column)

    if len(missing_columns) == 0:
        print("All expected variables are present.")
    else:
        print("Missing variables:", missing_columns)

    if data.isnull().sum().sum() == 0:
        print("No missing values found.")
    else:
        print("Missing values were found.")

    print("Data validation complete.")

def show_age_analysis():
    print()
    print("Age Group Analysis")

    for age in sorted(data["Age"].unique()):
        group = data[data["Age"] == age]

        print()
        print("Age", age)
        print("  Records:", len(group))
        print("  Average BMI:", round(group["BMI"].mean(), 2))
        print("  Average Sleep:", round(group["Sleep_Hours"].mean(), 2))
        print("  Average Exercise:", round(group["Exercise_Hours"].mean(), 2))
        print("  Average Heart Rate:", round(group["Heart_Rate"].mean(), 2))

def show_correlation_matrix():
    print()
    print("Correlation Matrix")
    print()

    correlations = data[
        ["Age", "BMI", "Sleep_Hours", "Exercise_Hours", "Heart_Rate"]
    ].corr()

    print(correlations.round(2))
    
def show_distribution():
    print()
    print("Distribution Analysis")
    print()
    print("BMI:")
    print(data["BMI"].describe().round(2))

    print()
    print("Sleep Hours:")
    print(data["Sleep_Hours"].describe().round(2))

    print()
    print("Exercise Hours:")
    print(data["Exercise_Hours"].describe().round(2))

    print()
    print("Heart Rate:")
    print(data["Heart_Rate"].describe().round(2))

def show_histograms():
    variables = [
        ("BMI", "BMI Distribution"),
        ("Sleep_Hours", "Sleep Hours Distribution"),
        ("Exercise_Hours", "Exercise Hours Distribution"),
        ("Heart_Rate", "Heart Rate Distribution")
    ]

    for column, title in variables:
        plt.hist(data[column], bins=6)
        plt.xlabel(column)
        plt.ylabel("Number of Records")
        plt.title(title)
        plt.show()

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

def show_menu():
    print()
    print("1. View summary statistics")
    print("2. View dataset information")
    print("3. View sleep and heart rate graph")
    print("4. View exercise and BMI graph")
    print("5. View correlations")
    print("6. Validate data")
    print("7. View age analysis")
    print("8. View correlation matrix")
    print("9. View distributions")
    print("10. View histograms")
    print("11. Exit")

print("Health Data Analyzer")

while True:
    show_menu()
    choice = input("Choose an option: ").strip()

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
        validate_data()
    elif choice == "7":
        show_age_analysis()
    elif choice == "8":
        show_correlation_matrix()
    elif choice == "9":
        show_distribution()
    elif choice == "10":
        show_histograms()
    elif choice == "11":
        print("Goodbye!")
        break
    else:
        print("Please choose a number from 1 to 11.")