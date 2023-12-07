

# In this Challenge, you are tasked with creating a Python script to analyse the  nancial records of your company.
# You will be given a  financial dataset called  budget_data.csv . The dataset is composed of two columns: "Date" and "Pro t/Losses".

# Your task is to create a Python script that analyses the records to calculate each of the following values:
# The total number of months included in the dataset
# The net total amount of "Pro t/Losses" over the entire period
# The changes in "Profit/Losses" over the entire period, and then the average of those changes
# The greatest increase in pro ts (date and amount) over the entire period
# The greatest decrease in pro ts (date and amount) over the entire period

#Importing the necessary modules/libraries
import os
import csv

# Set path to collect data from Resources folder
budget_data_csv = os.path.join('e:/UWA_BootCamp/python-challenge/PyBank','Resources', 'budget_data.csv')

# Set variables 
profits = []
dates = []
total_months = 0
total_pl_amount = 0
pl_value = 0
change = 0

# Open and read CSV File
with open (budget_data_csv, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    #Read header row and assign to variable csv_header
    csv_header = next(csvreader)

    # Read first row to track changes
    first_row = next(csvreader)

    #The total number of months included in the dataset
    #counting total months with increments of variable total_months
    total_months +=1
  
    # Update PL value for the next iteration
    pl_value = int (first_row[1])

    total_pl_amount += int (first_row[1])

    # Looping through each row after the first row data
    for row in csvreader:
        # Store date in the dates list
        dates.append(row[0])

        # Calculate PL for each transactions
        for i in range (len(row)):
            if i > 0:
                change = int(row[1]) - pl_value
                pl_value = int(row[1])
                profits.append(change)

                # Total months
                total_months += 1


# The net total amount of "Profit/Losses" over the entire period
                total_pl_amount = total_pl_amount + int (row[1])

# The changes in "Profit/Losses" over the entire period, and then the average of those changes
average_pl_changes = sum(profits)/len(profits)

# The greatest increase in profits (date and amount) over the entire period
greatest_pl_increase_amount = max(profits)
greatest_pl_increase_index = profits.index(greatest_pl_increase_amount)
greatest_pl_increase_date = dates[greatest_pl_increase_index]


# The greatest decrease in pro ts (date and amount) over the entire period
greatest_pl_decrease_amount = min(profits)
greatest_pl_decrease_index = profits.index(greatest_pl_decrease_amount)
greatest_pl_decrease_date = dates[greatest_pl_decrease_index]

# Displaying Analysis
print("Financial Analysis")
print("- ----------------------------")
print(f"Total Months: {str(total_months)}")
print(f"Total: ${str(total_pl_amount)}")
#This line rounds the average profit change to two decimal places.
print(f"Average Change: $(str{round(average_pl_changes,2)})")    
print(f"Greatest Increase in Profit: {greatest_pl_increase_date} (${str(greatest_pl_increase_amount)})")
print(f"Greatest Decrease in Profit: {greatest_pl_decrease_date} (${str(greatest_pl_decrease_amount)})")


# In addition, your final script should both print the analysis to the terminal and export a text file with the results.
output = open("output.txt", "w")

line1 = "Financial Analysis"
line2 = "-----------------------------"
line3 = str(f"Total Months: {str(total_months)}")
line4 = str(f"Total: ${str(total_pl_amount)}")
line5 = str(f"Average Change: $(str{round(average_pl_changes,2)})")    
line6 = str(f"Greatest Increase in Profit: {greatest_pl_increase_date} (${str(greatest_pl_increase_amount)})")
line7 = str(f"Greatest Decrease in Profit: {greatest_pl_decrease_date} (${str(greatest_pl_decrease_amount)})")

# writes the content of each line to the file, seperated by newlines
output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4,line5,line6,line7))
