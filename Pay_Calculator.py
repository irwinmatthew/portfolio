salary_per_hour = float(input("Enter Hourly Rate:")) #Change to your rate of pay
salary_overtime_rate = salary_per_hour * 1.5 #Calculates overtime pay at rate of 1.5x

hours_worked = int(input("Enter hours worked"))

overtime_hours = hours_worked - 40 #Hours over 40 is considered overtime
standard_hours = 40 - hours_worked #Hours under 40 is considered standard
salary_straight = hours_worked * salary_per_hour #Calculates salary for standard hours
salary_overtime = overtime_hours * salary_overtime_rate #Calculates salary for overtime

if hours_worked < 40:
    standard_hours = hours_worked
    print("You worked ", standard_hours, " hours of standard pay.")
    print("This earns $", salary_straight, " .")
elif hours_worked == 40:
    print("You worked ", hours_worked, " hours of standard pay.")
    print("This earns $", salary_straight, " .")
elif hours_worked > 40:
    overtime_hours = hours_worked - 40 #Calculate overtime hours
    standard_hours = 40 #Sets standard hours to 40, as anything over is overtime
    salary_straight = standard_hours * salary_per_hour
    total_pay = salary_overtime + salary_straight #Combines standard and overtime pay
    print("You worked ", overtime_hours, " hours of overtime pay and ", standard_hours, " hours of standard pay.")
    print("This earns $", salary_overtime, " of overtime and $", salary_straight, " of standard.")
    print("You earned $", f"{total_pay:.2f}", " before deductions.")
    
    


    
