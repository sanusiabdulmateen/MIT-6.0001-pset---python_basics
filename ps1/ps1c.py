# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 21:57:31 2023

@author: sanus
"""

starting_salary = int(input("Enter the starting salary: "))
# total amount of salary per year
total_cost = 1000000
# total cost of the house that you are saving for
portion_down_payment = 250000
# cost needed for a down payment
semi_annual_raise = 0.07
# the percentage by which the salary is increased every six month
rate = 0.04 
# rate of investment return per annum 
max_months = 36 
# max number of months to save for down payment
steps = 0 
# steps in bisection search
found = False 
# flag to find the best rate
min_rate = 0   #0%
max_rate = 10000   #100%


while abs(min_rate - max_rate) > 1:
    best_rate = int((min_rate + max_rate) / 2)
    # best saving rate
    steps += 1
    annual_salary = starting_salary
    monthly_savings = (best_rate / 10000) * (annual_salary / 12.0)
    current_savings = 0.0

    for months in range (1, max_months + 1):
        monthly_returns = (current_savings *  rate ) / 12
        # accounting for the increased value of the current savings
        current_savings += monthly_savings + monthly_returns
        # adding accumulated monthly investment and savings
        

        if abs(current_savings - portion_down_payment) < 100:
            min_rate = max_rate
            found = True
            break

        elif current_savings > portion_down_payment + 100:
            break

        if months % 6 == 0: 
            annual_salary += (semi_annual_raise * annual_salary)
            # addition of the semi annual increase in the salary
            monthly_savings = (best_rate / 10000) * (annual_salary / 12.0)
            # accounting for the increased value of the monthly salary

    if current_savings < portion_down_payment - 100:
        min_rate = best_rate
        
    elif current_savings > portion_down_payment + 100:
        max_rate = best_rate
    

if found:
    print("Best savings rate:", best_rate / 10000)
    print("Steps in bisection search:", steps)
else:
    print("It is not possible to pay the down payment in three years.")
