import locale
from interest import investment_value, years_to_reach_goal

locale.setlocale(locale.LC_ALL, 'en_US')  # Set locale for currency formatting

print("Welcome to the interest app!")

while True:
    option = input("What would you like to do? Enter 'value', 'goal', or 'exit': ")
    option = option.strip().lower()
    match option:
        case "value":
            start = float(input("Enter the starting amount: "))
            tax_rate = float(input("Enter the tax rate (as a decimal): "))
            years = int(input("Enter the number of years: "))
            interest_rate = float(input("Enter the interest rate (as a decimal): "))
            deposit = float(input("Enter the annual deposit amount: "))
            funds = investment_value(start, interest_rate, years, tax_rate, deposit)
            print(locale.currency(funds, grouping=True))
        case "goal":
            start = float(input("Enter the starting amount: "))
            tax_rate = float(input("Enter the tax rate (as a decimal): "))
            interest_rate = float(input("Enter the interest rate (as a decimal): "))
            deposit = float(input("Enter the annual deposit amount: "))
            goal = float(input("Enter the goal amount: "))
            years_needed = years_to_reach_goal(start, interest_rate, tax_rate, deposit, goal)
            print(f"It will take {years_needed} years to reach your goal.")
        case "exit":
            print("Thank you for using the interest app!")
            break
        case _:
            print("Invalid option. Please try again.")