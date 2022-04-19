# Import dependences to read the csv file
import os
import csv

# Retrieve the csv file
budget_csv = os.path.join("Resources", "budget_data.csv")

# Create an empty list to store the increases and decreases
change = []

# Create variables total months, net total, and net change
total_months = 0
net_total = 0
net_change = 0 
greatest_increase = 0
greatest_decrease = 0 

# Read the csv file
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    
    # Initialize variables for our loop
    row = next(csvreader)
    previous_row = int(row[1])
    net_total += int(row[1])
    total_months += 1

    # Loop through the csv file
    for row in csvreader:
        
        # Calculate the total months
        total_months += 1

        # Calculate the net total
        net_total = net_total + int(row[1])

        # Calculate the net change between consecutive values
        net_change = int(row[1]) - previous_row

        # Append the net changes to a list
        change.append(net_change)

        # Set the previous row to be the current row before the next loop iteration
        previous_row = int(row[1])

        # Create a variable that holds the average change 
        avg_change = sum(change) / len(change)

        # Create conditional statement to find the greatest increase
        if net_change > greatest_increase:
            greatest_increase = net_change
            greatest_increase_month = row[0]

        # Create conditional statement fo find the greatest decrease
        if net_change < greatest_decrease:
            greatest_decrease = net_change
            greatest_decrease_month = row[0]

# Create a string to print the results
Financial_Analysis = f'''
  Financial Analysis
  ----------------------------
  Total Months: {total_months}
  Total: ${net_total}
  Average Change: ${avg_change:.2f}
  Greatest Increase in Profits: {greatest_increase_month}, ${greatest_increase:.2f}
  Greatest Decrease in Profits: {greatest_decrease_month}, ${greatest_decrease:.2f}
  '''
print(Financial_Analysis)

# Export the final report to a text file
with open("Analysis/budget_data.txt", "w") as Budget_Analysis: 
    Budget_Analysis.write(Financial_Analysis)