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
pybank_path_CSV = os.path.join("..", "Resources", "budget_data .csv")

#open the file in "read" mode
with open(pybank_path_CSV) as paybank_csvfile:
    print(paybank_csvfile)


total_month = []
total_amout = []

