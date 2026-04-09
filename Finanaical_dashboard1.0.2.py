# The function that calculates the number of months based on user input in current savings, monthly contribution and goal
# Then returns the number of months needed to reach goal and gets it by running a loop until current savings reaches goal

def get_vaild_input(prompt_message):
    while True: 
        try: 
            user_input = float(input(prompt_message))
            return user_input 
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

def compute_months():
        month = 0 
        current_savings = get_vaild_input("Enter your current savings: ")
        monthly_contribution = get_vaild_input("Enter your monthly contribution: ")
        goal = get_vaild_input("Enter your savings goal: ")
        
        while current_savings < goal:
            month += 1
            current_savings += monthly_contribution
        return month, current_savings, monthly_contribution, goal

# the functions that calculates the furture value of investment/savings 
# bases it the on current savings, monthly contribution and anual rate of return
def monthly_investment():
        Months = get_vaild_input("Enter the number of months you want to invest: ")
        current_savings = get_vaild_input("Enter your current savings: ")
        monthly_contribution = get_vaild_input("Enter your monthly contribution: ")
        annual_rate = get_vaild_input("Enter your annual rate of return: ")
        for i in range(int(Months)):
            current_savings += monthly_contribution 
            current_savings += (current_savings * annual_rate / 12 / 100)
        return current_savings, Months

# fucntions to calculate the monthly contribution needed to reach saving goal  
def contrubution_calculator():
        Months = get_vaild_input("Enter the number of months you want to invest: ")
        goal = get_vaild_input("Enter your savings goal: ")
        current_savings = get_vaild_input("Enter your current savings: ")
        annual_rate = get_vaild_input("Enter your annual rate of return: ")
        month_rate = annual_rate / 12 / 100
        future_value = current_savings * (1 + month_rate) ** Months 
        needed_savings = goal - future_value 
        Payment = needed_savings * month_rate / (((1 + month_rate) ** Months) - 1)
        return Payment, Months
# function to calculate the total interest earned on an investment
def Interest_calculator():
        Month = get_vaild_input("Enter the number of months you want to invest: ")
        current_savings = get_vaild_input("Enter your current savings: ")
        monthly_contribution = get_vaild_input("Enter your monthly contribution: ")
        annual_rate = get_vaild_input("Enter your annual rate of return: ")
        month_rate = annual_rate / 12 / 100
        total_pricipal = current_savings + (monthly_contribution * Month)
        balance = current_savings
        for i in range(int(Month)):
            balance += monthly_contribution
            balance += (balance * month_rate)
        interest_earned = balance - total_pricipal
        return interest_earned, Month

#----------------------- main dashboard -----------------------#
# This is the main dashbord to choose the financial simulation you want to run
def main():
        print("Welcome to the Financial Simulation Dashboard!")
        print("----------------------------------------------")
        while True:
            try:
                Options = int(input(
                "1. Calculate the number of months to reach a savings goal. \n"
                "2. Calculate the future value of an investment. \n"
                "3. Calculate the monthly contribution needed to reach a savings goal. \n"
                "4. Calculate the total interest earned on an investment. \n"
                "5. Exit \n"))
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                continue
                # The first selection to caluclate the number of months 
            if Options == 1:
                print("Selcted Month Calculator")
                results = compute_months()
                print(f"The amount of months to reach that goals is: {results[0]:,.2f} months")

            elif Options == 2:
                print("Selected Furture Value Calculator")
                results = monthly_investment()
                print(f"The total after {int(results[1])} months is {results[0]:,.2f}")

            #The third section is more striaght foward with calulating the contribution by using 
            #final goal minus current savings and how many month you wanted to invest to get a exact number of month needed to reach the goal
            elif Options == 3:
                print("selected Contriution calculator")
                results = contrubution_calculator()
                print(f"The fianical contribution needed in {results[1]} months to reach your goal is: {results[0]:,.2f}")

            elif Options == 4:
                print("selected Interest calculator")
                results = Interest_calculator()     
                print(f"The total interest earned on your investment is {results[0]:,.2f}")
                
            elif Options == 5:
                print("Thank you for using the Financial Simulation Dashboard. Goodbye!")
                exit()

            else:
                print("Invalid input. Please select a valid option from the menu.")

if __name__ == "__main__":
        main() 
