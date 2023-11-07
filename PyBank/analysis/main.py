import os

import csv
csvpath = os.path.join('..', 'analysis', 'budget_data.csv')

# Initialize variables to store data
total_months = 0
net_total = 0
previous_profit = None
changes = []
greatest_increase = 0
greatest_decrease = 0

# Open and read the CSV file
with open("budget_data.csv", 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)  # Skip the header row

    for row in csvreader:
        date, profit = row
        profit = int(profit)

        # Calculate total months and net total
        total_months += 1
        net_total += profit

        # Calculate changes and find greatest increase and decrease
        if previous_profit is not None:
            change = profit - previous_profit
            changes.append(change)
            if change > greatest_increase:
                greatest_increase = change
                greatest_increase_date = date
            if change < greatest_decrease:
                greatest_decrease = change
                greatest_decrease_date = date
        previous_profit = profit

# Calculate the average change
average_change = sum(changes) / len(changes)

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")
