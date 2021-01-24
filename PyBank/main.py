# create a Python script that analyzes the records to calculate each of the following:
# 1. The total number of months included in the dataset
# 2. The net total amount of "Profit/Losses" over the entire period
# 3. Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
# 4. The greatest increase in profits (date and amount) over the entire period
# 5. The greatest decrease in losses (date and amount) over the entire period

# ------------------------------------------------------
# Import dependencies
import os
import csv

#path to financial data and output 
pybank_path_csv = os.path.join("Resources", "budget_data .csv")
pybank_output_csv = os.path.join("Output", "budget_data.txt")

# create a list
month = []
profit = []
monthly_change = []

# define variables
count = 0
inital_profit = 0
total_change_profit= 0
total_profit = 0


#open the file in "read" mode
with open(pybank_path_csv) as pybank_csvfile:
   csvreader = csv.reader(pybank_csvfile, delimiter=",")
#    print(csvreader)
   csv_header = next(pybank_csvfile)
#    print(f"csv_header:{csv_header}")
       
   for row in csvreader:
        # print(row)
        count = count + 1
        month.append(row[0])
        profit.append(row[1])
        total_profit = total_profit + int(row[1])

        final_profit = int(row[1])
        monthly_change_profit = inital_profit - final_profit 
        monthly_change.append(monthly_change_profit)
        
        total_change_profit = total_change_profit + monthly_change_profit

        inital_profit = final_profittotal_profittotal_profit

        # Calculate the average change
        average_change_profit = (total_change_profit/count)
        
        # Find the max and min change in profits and its month
        Max_profit_change = max(monthly_change)
        Min_profit_change = min(monthly_change) 
            
        Max_profit_change_month = month[monthly_change.index(Max_profit_change)]
        Min_profit_change_month = month[monthly_change.index(Min_profit_change)]

# Print the analysis
print("Financial Analysis")
print("----------------------------")
print(f"Total Months:  {count}")
print(f"Total:  ${total_profit}")
print(f"Average Change:  ${average_change_profit}")
print(f"Greatest Increase in Profits:  {Max_profit_change_month} (${Max_profit_change})")
print(f"Greatest Decrease in Losses:  {Min_profit_change_month} (${Min_profit_change})")

# Export a text file
pybank_output_csv = os.path.join("Output", "budget_data.txt")
with open(pybank_output_csv, "w") as text_file:
            text_file.write(
                f"Financial Analysis: \n"
                f"----------------------------\n"
                f"Total Months: {count}\n" 
                f"Total : ${total_profit}\n"
                f"Average Change: ${average_change_profit}\n"
                f"Greatest Increase in Profit: {Max_profit_change_month} (${Max_profit_change})\n"
                f"Greatest Decrease in Losses: {Min_profit_change_month} (${Min_profit_change})\n"
                )