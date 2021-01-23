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
pybank_output_csv = os.path.join("Output", "budget_data.text")

# define variables
total_month = []
total_amount = []

count_month = 0
net_profit_loss = 0
previous_month_profit_loss = 0
current_month_profit_loss = 0
profit_losses_change = 0


#open the file in "read" mode
with open(pybank_path_csv) as pybank_csvfile:
   csvreader = csv.reader(pybank_csvfile, delimiter=",")
   #print(csvreader)
   csv_header = next(pybank_csvfile)
   #print(f"csv_header:{csv_header}")
   for row in csvreader:
       #print(row)
     count_month += 1
     current_month_profit_loss = int(row[1])
     net_profit_loss += current_month_profit_loss

    #  print(current_month_profit_loss)
    #  print(count_month)
    #  print(net_profit_loss)

if (count_month == 1):
    previous_month_profit_loss = current_month_profit_loss
else:
    profit_losses_change = current_month_profit_loss - previous_month_profit_loss
    total_month.append(row[0])
    total_amount.append(row[1])
    #reset
    previous_month_profit_loss = current_month_profit_loss
  
    # print(count_month)
    # print(profit_losses_change)
    # print(net_profit_loss)

# The average of "Profit/Losses" over the entire period
    average = round(net_profit_loss/(count_month -1), 2)
    # print(average)

# The greatest increase/decrease in profits (date and amount) over the entire period
    greatest_increase = max(total_amount)
    greatest_decrease = min(total_amount)
    # print(greatest_increase)
    # print(greatest_decrease)
# Locate the index value of increase/decrease
    greatest_increase_month_index = total_amount.index(greatest_increase)
    greatest_decrease_month_index = total_amount.index(greatest_decrease)

# Assign greatest increase/decrease month
    greatest_increase_month = total_month[greatest_increase_month_index]
    greatest_decrease_month = total_month[greatest_decrease_month_index]

# Print the analysis
print("Financial Analysis")
print("----------------------------")
print(f"Total Months:  {count_month}")
print(f"Total:  ${net_profit_loss}")
print(f"Average Change:  ${average}")
print(f"Greatest Increase in Profits:  {greatest_increase_month} (${greatest_increase_month_index})")
print(f"Greatest Decrease in Losses:  {greatest_decrease_month} (${greatest_decrease_month_index})")

# Export a text file
pybank_output_csv = os.path.join("Output", "budget_data.text")
with open(pybank_output_csv, "w") as text_file:
            text_file.write(
                f"Financial Analysis: \n"
                f"----------------------------\n"
                f"Total Months: {count_month}\n" 
                f"Total : ${net_profit_loss}\n"
                f"Average Change: ${average}\n"
                f"Greatest Increase in Profit: {greatest_increase_month} (${greatest_increase_month_index})\n"
                f"Greatest Decrease in Losses: {greatest_decrease_month} (${greatest_decrease_month_index})\n"
            )