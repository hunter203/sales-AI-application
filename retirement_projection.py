# Simple Retirement Projection Application
# This script calculates projected retirement savings and compares them to
# estimated averages for US households. Results are displayed as graphs.

import matplotlib.pyplot as plt

# Sample average savings by age group in the USA (values in thousands of dollars).
# These numbers are illustrative and not from a specific dataset.
AVERAGE_SAVINGS_BY_AGE = {
    30: 40,
    40: 120,
    50: 210,
    60: 330,
    70: 400,
}


def compound_growth(present_value, annual_contrib, rate, years):
    """Compute future value of a series of cash flows."""
    value = present_value
    for _ in range(years):
        value = (value + annual_contrib) * (1 + rate)
    return value


def adjust_for_inflation(amount, inflation_rate, years):
    """Adjust a nominal amount for inflation."""
    return amount / ((1 + inflation_rate) ** years)


def project_retirement(age, retirement_age, current_savings, annual_contrib,
                        return_rate, inflation_rate):
    years = retirement_age - age
    nominal = []
    real = []
    ages = []

    value = current_savings
    for i in range(years + 1):
        ages.append(age + i)
        nominal.append(value)
        real_value = adjust_for_inflation(value, inflation_rate, i)
        real.append(real_value)
        value = (value + annual_contrib) * (1 + return_rate)

    return ages, nominal, real


def plot_projection(user_ages, user_nominal, user_real):
    plt.figure(figsize=(10, 6))

    plt.plot(user_ages, user_nominal, label="Your Savings (Nominal)")
    plt.plot(user_ages, user_real, label="Your Savings (Real)")

    # Plot average savings for comparison
    avg_ages = sorted(AVERAGE_SAVINGS_BY_AGE.keys())
    avg_values = [AVERAGE_SAVINGS_BY_AGE[a] * 1000 for a in avg_ages]
    plt.plot(avg_ages, avg_values, label="Estimated US Average", linestyle="--")

    plt.xlabel("Age")
    plt.ylabel("Savings ($)")
    plt.title("Retirement Savings Projection")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    # Basic example values
    AGE = 35
    RETIREMENT_AGE = 65
    CURRENT_SAVINGS = 50000  # dollars
    ANNUAL_CONTRIB = 10000   # dollars per year
    RETURN_RATE = 0.05       # 5% annual return
    INFLATION_RATE = 0.02    # 2% annual inflation

    user_ages, nominal, real = project_retirement(
        AGE,
        RETIREMENT_AGE,
        CURRENT_SAVINGS,
        ANNUAL_CONTRIB,
        RETURN_RATE,
        INFLATION_RATE,
    )

    plot_projection(user_ages, nominal, real)
