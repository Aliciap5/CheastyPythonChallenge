import os
import csv

# Path to collect data
file = os.path.join("budget_data.csv")

total_months = 0
total_profit = 0
monthly_avg_profit = 0
greatest_inc = 0
greatest_inc_month = ""
greatest_dec = 0
greatest_dec_month = ""

prev_pl = 0
changes = []


with open(file, "r") as data:
    csvreader = csv.reader(data, delimiter = ",")
    header = next(csvreader)
    for row in csvreader:
        date = row[0]
        pl = int(row[1])
        total_profit += pl
        total_months += 1

        change = pl - prev_pl
        if total_months != 1:
            changes.append(change)
        if change > greatest_inc:
            greatest_inc = change
            greatest_inc_month = date
        if change < greatest_dec:
            greatest_dec = change
            greatest_dec_month = date
        
        prev_pl = pl




avg_change= sum(changes)/len(changes)






monthly_avg_profit = int(round(total_profit/total_months,0))
analysis = f"""
Finalcial Analysis
----------------------------------------------
Total Profit: $ {total_profit}
Total Months: {total_months}
Average Monthly Change: $ {monthly_avg_profit}
Greatest Increase: {greatest_inc_month}, $ {greatest_inc}
Greatest Decrease: {greatest_dec_month}, $ {greatest_dec}"""

print(analysis)

output = "output.csv"