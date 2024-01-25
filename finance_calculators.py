"""Module has a function which calculates bond monthly repayments or
 simple and compound interest investment"""
import math

# Asking user to input investment or bond
print("investment - to calculate the amount of interest \
you'll earn on your investment")
print("bond       - to calculate the amount you'll have to pay on a home loan")
print("")
user_select = input("Enter either 'investment' or 'bond' \
from the menu above to proceed: ").lower()

# Beginning of if, elif, else to determine if user input is valid
if user_select == "bond":
    print("Thank you for selecting bond.")
# Beginning 'bond' input, asking user to input bond details and
# storing as float variables
    house_value = float(input("What is the present value of the house: "))
    bond_interest = float(input("What is the interest rate (in %): "))/100/12
    number_of_months = float(input("How many months do you plan to repay: "))
# Calculating monthly repayments from user's previous inputs
    repayment = (bond_interest*house_value)/  \
                (1-(1 + bond_interest)**(-number_of_months))
    print(f"Each month you will have to repay: £{repayment:.2f}")

elif user_select == "investment":
    print("Thank you for selecting investment.")
# Beginning of 'investment' input, asking user to input investment details
# and storing as float variables
    amount_deposited = float(input("How much would you like to deposit: "))
    investment_interest = float(input("What is the interest rate (in %): "))/100
    number_of_years = float(input("How many years do you plan on investing: "))
    interest = input("Would you like 'simple' or 'compund' interest: ").lower()

    if interest == "simple":
# Beginning of 'simple' investment input, calculating simple interest from
# user's previous inputs
        simple_interest = amount_deposited *\
                        (1 + investment_interest*number_of_years)
        print(f"The total amount once interest has \
been applied is: £{simple_interest:.2f}")

    elif interest == "compound":
# Beginning of 'compound' investment input, calculating compound interest
# from user's previous inputs
        compound_interest = amount_deposited * math.pow((1 +
                            investment_interest),number_of_years)
        print(f"The total amount once interest has \
been applied is: £{compound_interest:.2f}")

# Error print if user input is invalid (not simple or compound)
    else:
        print("Error - Please choose either 'simple' or 'compound' interest.")

# Error print if user input if invalid (no investment or bond)
else:
    print("Error - Please choose either 'investment' or 'bond'.")
