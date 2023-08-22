# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 21:57:31 2023

@author: sanus
"""

starting_salary = int(input("Enter the starting salary: "))
total_cost = 1000000
semi_annual_raise = 0.07 
# the percentage by which the salary is increased every six month - 7%
portion_down_payment = 0.25 * total_cost
# cost needed for a down payment
rate = 0.04   # annual investment rate = 4%
best_rate = 0 # best rate for saving
max_rate = 10000
min_rate = 0
best_rate = (min_rate + max_rate) / 2
found = False
steps = 0
max_months = 36

while abs(min_rate - max_rate) > 1:
    best_rate_used = best_rate / 10000
    
    monthly_salary = starting_salary / 12
    monthly_addition = best_rate_used * monthly_salary
    current_savings = 0.00
    monthly_return = current_savings * ( rate / 12 )
    # monthly investment return of the current savings
    
    for months in range(max_months):
            
            monthly_return = current_savings * ( rate / 12 )
            # accounting for the increased value of the current savings
            current_savings += monthly_addition + monthly_return
            # adding accumulated monthly investment and savings
            
            if abs(current_savings - portion_down_payment) < 100:
                min_rate = max_rate
                found = True
                break
            
            elif current_savings > portion_down_payment + 100:
                break
            
            if months != 0 and months % 6 == 0:
                monthly_salary += semi_annual_raise * monthly_salary
                # addition of the semi annual increase in the salary
                monthly_addition = best_rate_used * monthly_salary
                # accounting for the increased value of the monthly salary
            
    if current_savings - portion_down_payment < 100:
        min_rate = best_rate
    else:
        max_rate = best_rate
    best_rate = (min_rate + max_rate) / 2
    
    steps += 1
    

if found:
    print("Best saving rate:", best_rate_used)
    print("Steps in bisection search:", steps)
else:
    print("It is not possible to pay the down payment in three years.")
        
        
        
        
        
        
       