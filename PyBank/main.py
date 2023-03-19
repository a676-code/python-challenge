# main.py
# Andrew Lounsbury
# 3/16/23
# Purpose: module 3 for Vanderbilt Data Analytics Bootcamp; processes data in the given budget_data.csv file
import os, csv

# getting the path to budget_data.csv
csvpath = os.path.join('Resources', 'budget_data.csv')

# opening and reading budget_data.csv
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # storing the header
    csv_header = next(csvreader)
    
    # looping through the records, computing net change, minimum change, and maximum change, storing both the value and the date
    numMonths = 0
    netChange = 0
    maxChange = -1
    minChange = 999999999999
    for row in csvreader:
        numMonths += 1
        netChange += int(row[1])
        if int(row[1]) > maxChange:
            maxChangeDate = row[0]
            maxChange = int(row[1])
        if int(row[1]) < minChange:
            minChangeDate = row[0]
            minChange = int(row[1])
    
    # computing the average change and rounding it to the second decimal place
    average = round(netChange / numMonths, 2)
    
    # printing the results
    print("Financial Analysis")
    print("-----------------------------------")
    print("Total Months: " + str(numMonths))
    print("Total: $" + str(netChange))
    # The following line prints the average with 2 decimal places so that it prints $262374.40 rather than $262374.4
    print("Average Change: $" + "{:.2f}".format(average))
    print("Greatest Increase in Profits: " + maxChangeDate + " ($" + str(maxChange) + ")")
    print("Greatest Decrease in Profits: " + minChangeDate + " ($" + str(minChange) + ")")
    
    # writing the results to pybank_results.txt
    file = open("analysis/pybank_results.txt", 'w')
    file.write("Financial Analysis\n")
    file.write("-----------------------------------\n")
    file.write("Total Months: " + str(numMonths))
    file.write("\nTotal: $" + str(netChange))
    file.write("\nAverage Change: $" + str(netChange / numMonths))
    file.write("\nGreatest Increase in Profits: " + maxChangeDate + " ($" + str(maxChange) + ")")
    file.write("\nGreatest Decrease in Profits: " + minChangeDate + " ($" + str(minChange) + ")")
    file.close()