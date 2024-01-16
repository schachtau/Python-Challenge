import os
import csv


budget_csv = os.path.join('Resources','budget_data.csv')
output_file = "analysis/financial_analysis.txt"


total_months = 0
total_amount = 0
changes = []
greatest_increase = {"date": None, "amount": float('-inf')}
greatest_decrease = {"date": None, "amount": float('inf')}

with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    previous_value = None

    for row in csvreader:
        date = row[0]
        profit_loss = int(row[1])
        total_months += 1
        total_amount += profit_loss

        if previous_value is not None:
            change = profit_loss - previous_value
            changes.append(change)

            if change > greatest_increase["amount"]:
                greatest_increase["date"] = date
                greatest_increase["amount"] = change

            if change < greatest_decrease["amount"]:
                greatest_decrease["date"] = date
                greatest_decrease["amount"] = change

        previous_value = profit_loss

# Calculate the average change
average_change = round(sum(changes) / len(changes), 2)

# Generate the financial analysis report
financial_analysis = (
    "Financial Analysis\n"
    "----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_amount}\n"
    f"Average Change: ${average_change}\n"
    f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})\n"
    f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})\n"
)

# Print the analysis to the terminal
print(financial_analysis)

# Export the analysis to a text file
with open(output_file, "w") as textfile:
    textfile.write(financial_analysis)

print("Financial analysis saved to 'financial_analysis.txt'.")



