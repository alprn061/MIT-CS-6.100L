## 6.100A PSet 1: Part A
## Name:
## Time Spent:
## Collaborators:

##################################################################################
## Get user input for yearly_salary, portion_saved and cost_of_dream_home below ##
##################################################################################
# get the yearly salary from user
yearly_salary = float(input("What is your yearly salary : $"))
# get the portion percantage from user
portion_saved = float(input("What is your portion of salary to be saved as percantage : %"))/100
# get the cost of dream house from user
cost_of_dream_home = float(input("What is the cost of your dream house : "))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################
# set the percentage of the total cost needed for a down payment
portion_down_payment = 0.25
# total amount of saved until today
amount_saved = 0
# annual rate of retunr
r = 0.05
# monthly salary
monthly_salary = yearly_salary/12
# monthly salary saving
monthly_saving = monthly_salary * portion_saved
monthly_rate = r/12

###############################################################################################
## Determine how many months it would take to get the down payment for your dream home below ## 
###############################################################################################
# initial savement
total_sav = 0
# just started work
month_passed = 0

while (total_sav <= cost_of_dream_home*portion_down_payment):   #save unless it equals to down payment
    total_sav = (total_sav) + (total_sav * monthly_rate) + (monthly_salary*portion_saved)    # total saving increase every month by previous saving + interest rate of return of previous month + existing month monthly salary portion saved  
    month_passed +=1  # month count
    

print(f"Number of months: {month_passed}")
