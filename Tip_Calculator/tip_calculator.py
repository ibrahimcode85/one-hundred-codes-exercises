# Welcome message
print("Welcome to the tip calculator.")

# 1. Get the total bill
total_bill = float(input("What was the total bill? $"))

# 2. Get the tip percentage
tips_percent = float(input("What percentage tip would you like to give? 10%, 12% or 15%?"))

# 3. Number of people to split
num_ppl = int(input("How many people to split the bill?"))

# 4. Calculate the amount each person should pay
amount_to_pay = round(total_bill * (1 + tips_percent / 100) / num_ppl,2)

# 5. Print message
print(f"Each person should pay ${amount_to_pay}")