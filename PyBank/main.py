#The total number of months included in the dataset
#The net total amount of "Profit/Losses" over the entire period
#Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in losses (date and amount) over the entire period

#------------------------------------------------------
# Import dependencies
import os
import csv

#path to financial data
pybank_path_CSV = os.path.join("Resources", "budget_data .csv")

# define variables
total_month = []
total_amount = []

#open the file in "read" mode
with open(pybank_path_CSV) as paybank_csvfile:
   csvreader = csv.reader(paybank_csvfile, delimiter=",")
   #print(csvreader)
   csv_header = next(csvreader)
   #print(f"csv_header:{csv_header}")
   for row in csvreader:
       #print(row)
    total_month.append(row[0])
    total_amount.append(row[1])
    print(total_month)



