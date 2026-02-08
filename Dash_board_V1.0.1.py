
# from ssl import Options
# import test_finance
# from . import test_finance


# The function that caluclates the number of months based on user input in current savings, monthly contrubution and goal
# Then returns the number of months needed to reach goal and gets it by running a loop until current savings reaches goal
def compute_months(current_savings, monthly_contribution, goal):
    month = 0
    while current_savings < goal:
        month += 1
        current_savings += monthly_contribution
    print(f"The amount of months to reach that goals is: {month} months")
    return month

# the functions that calculates the furture value of investment/savings 
# bases it the on current savings, monthly contribution and anual rate of return
def monthly_investment(current_savings, monthly_contribution, anual_rate):
    Months = int(input("Enter the number of months you want to invest: "))
    for i in range(Months):
        current_savings += monthly_contribution 
        current_savings += (current_savings * anual_rate / 12 / 100)
    print(f"The total after {i+1} months is {current_savings:,.2f}")
    return current_savings

# This is the main dashbord to choose the financial simulation you want to run
def main():  
    print("This is a financial simulation dashboard.")
    print("-----------------------------------------")
    Options = int(input(
    "1. Calculate the number of months to reach a savings goal. \n"
    "2. Calculate the future value of an investment. \n"
    "3. Calculate the monthly contribution needed to reach a savings goal. \n"
    "4. Calculate the total interest earned on an investment. \n"))

    # The first selection to caluclate the number of months 
    if Options == 1:
        print("Selcted Month Calculator")
        goal = int(input("Enter your savings goal: "))
        monthly_contribution = int(input("Enter your monthly contribution: "))
        if input("Do you having a current savings? (Y/N)") == "Y": 
            current_savings = int(input("Enter your Current Savings: "))
            compute_months(current_savings, monthly_contribution, goal)
        else:
            current_savings = 0
            compute_months(current_savings, monthly_contribution, goal)

    elif Options == 2:
        print("Selected Furture Value Calculator")
        current_savings = int(input("Enter your current savings: "))
        monthly_contribution = int(input("Enter your monthly contribution: ")) 
        annual_rate = float(input("Enter your annual rate of return: "))
        monthly_investment(current_savings, monthly_contribution, annual_rate)

    #The third section is more striaght foward with calulating the contribution by using 
    #final goal minus current savings and how many month you wanted to invest to get a exact number of month needed to reach the goal
    elif Options == 3:
        print("selected Contriution calculator")
        goal = int(input("Enter your savings goal: "))
        current_savings = int(input("Enter your current savings: "))
        annual_rate = int(input("Enter your annual rate of return: "))
        month_rate = annual_rate / 12/ 100
        Months = int(input("Enter the number of months you want to invest: "))
        future_value = current_savings * (1 + month_rate) ** Months 
        needed_savings = goal - future_value 
        Payment = needed_savings * month_rate / (((1 + month_rate) ** Months) - 1)
        print(f"The monthly contribution needed to reach your goal is: {Payment:,.2f}")

    elif Options == 4:
        print("selected Interest calculator")
        current_savings =int(input("Enter your current savings: "))
        monthly_contribution = int(input("Enter your monthly contribution: "))
        annuual_rate = float(input("Enter your annual rate of return: "))
        month_rate = annuual_rate /12 / 100
        Month = int(input("Enter the number of months you want to invest: "))
        total_pricipal = current_savings + (monthly_contribution * Month)
        balance = current_savings
        for i in range(Month):
            balance += monthly_contribution
            balance += (balance * month_rate)
        interest_earned = balance - total_pricipal
        print(f"The total interest earned on your investment is {interest_earned:,.2f}")
if __name__ == "__main__":
    main()
