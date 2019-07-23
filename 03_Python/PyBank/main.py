#importing libraries
import os
import csv

#Importing csv file
budget_csv = os.path.join("budget_data.csv")

# initialising variables
change = 0
total = 0
months = 0
great_inc = 0
great_dec = 0

# opening the csv
with open(budget_csv, newline = "") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')
    
    next(csv_reader)
    
    #looping through the csv
    for row in csv_reader:
        
        # Taking the net profit/loss
        total += int(row[1])
        
        # Counting the number of months
        months += 1
        
        # Taking the average change
        if months > 1:
            change += int(row[1]) - prev_month
        
            # Finding greatest increase
            if int(row[1]) - prev_month > great_inc:
                great_inc = int(row[1]) - prev_month
                great_inc_mon = row[0]

            # Finding greatest decrease
            if int(row[1]) - prev_month < great_dec:
                great_dec = int(row[1]) - prev_month
                great_dec_mon = row[0]
        
        # storing the last month's profit/loss
        prev_month = int(row[1])   
        
# Printing the results
print("Financial Analysis")
print("--------------------------------------")
print(f'Total Months: {months}')               
print(f'Total: ${total}')
print(f'Average Change: ${round(change/(months - 1),2)}')
print(f'Greatest Increase in Profits: {great_inc_mon} (${great_inc})')
print(f'Greatest Decrease in Profits: {great_dec_mon} (${great_dec})')

# Writing the results to a text file
text_file = open("Financial_Analysis.txt","w")
text_file.write(f"Financial Analysis\n")
text_file.write(f"------------------------------------------------\n")
text_file.write(f'Total Months: {months}\n')               
text_file.write(f'Total: ${total}\n')
text_file.write(f'Average Change: ${round(change/(months - 1),2)}\n')
text_file.write(f'Greatest Increase in Profits: {great_inc_mon} (${great_inc})\n')
text_file.write(f'Greatest Decrease in Profits: {great_dec_mon} (${great_dec})')
text_file.close()