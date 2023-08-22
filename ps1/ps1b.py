# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 18:45:36 2023

@author: sanus
"""

annual_salary = float(input("Enter your annual salary: "))
# total amount of salary per year
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
# portion of salary to be saved monthly
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the sem-annual raise, as a decimal: "))
# the percentage by which the salary is increased every six month
portion_down_payment = 0.25 * total_cost
# cost needed for a down payment
monthly_salary = annual_salary / 12
monthly_addition = portion_saved * monthly_salary
# portion of monthly salary to be saved
current_savings = 0.00
rate = 0.04   # annual investment rate = 4%
monthly_return = current_savings * ( rate / 12 )
# monthly investment return of the current savings
months = 0

while current_savings < portion_down_payment:
    if months != 0 and months % 6 == 0:
        monthly_salary += semi_annual_raise * monthly_salary
        # addition of the semi annual increase in the salary
        monthly_addition = portion_saved * monthly_salary
        # accounting for the increased value of the monthly salary
    
    current_savings += monthly_addition + monthly_return
    # adding accumulated monthly investment and savings
    monthly_return = current_savings * ( rate / 12 )
    # accounting for the increased value of the current savings
    months += 1
    
print("Number of months:", months)