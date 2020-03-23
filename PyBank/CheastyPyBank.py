#import modules
import os
import csv

# Create the function
def analyze_budgets(file):

    # Path to collect data
    file = os.path.join("budget_data.csv")

    #establish variables and initial values
    total_months = 0
    total_profit = 0
    monthly_avg_profit = 0
    greatest_inc = 0
    greatest_inc_month = ""
    greatest_dec = 0
    greatest_dec_month = ""

    prev_pl = 0
    changes = []

    # Read the CSV file
    with open(file) as data:
        csvreader = csv.reader(data, delimiter = ",")
        header = next(csvreader)
        
        # Create the for loop
        for row in csvreader:
            
            # set the location of the columns from the csv for those variables
            date = row[0]
            pl = int(row[1])

            #To set the total values from the csv
            total_profit += pl
            total_months += 1

            # Calculate the change from month to month with an if statement to skip change from nothing to first month
            change = pl - prev_pl
            if total_months != 1:
                changes.append(change)

            #Set the greatest increase values (both the amount and the month) as it loops through the change values
            if change > greatest_inc:
                greatest_inc = change
                greatest_inc_month = date

            #Set the greatest decrease values (both the amount and the month) as it loops through the change values
            if change < greatest_dec:
                greatest_dec = change
                greatest_dec_month = date
            
            # Reset the current month/value as the previous month for the next loop
            prev_pl = pl


    # Calculate the average of change values
    monthly_avg_profit = int(round(total_profit/total_months,0))

    # Create the output values and format
    analysis = f"""
    Finalcial Analysis
    ----------------------------------------------
    Total Profit: $ {total_profit}
    Total Months: {total_months}
    Average Monthly Change: $ {monthly_avg_profit}
    Greatest Increase: {greatest_inc_month}, $ {greatest_inc}
    Greatest Decrease: {greatest_dec_month}, $ {greatest_dec}"""

    # Print results to the terminal
    print(analysis)

    # to create an output text file
    # Specify the file to write and create the text file
    output_file="output.txt"
    with open(output_file, "w") as doc:
        doc.write(analysis)

# Create file path for csv import
path = os.path.join("Resources", "budget_data.csv")
# Run the function on the path
analyze_budgets(path)