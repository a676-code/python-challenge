import os, csv

csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    
    numMonths = 0
    netChange = 0
    maxChange = -1
    minChange = 9999999999
    for row in csvreader:
        numMonths += 1
        netChange += int(row[1])
        if int(row[1]) > maxChange:
            maxChangeDate = row[0]
            maxChange = int(row[1])
        if int(row[1]) < minChange:
            minChangeDate = row[0]
            minChange = int(row[1])
    
    print("Financial Analysis")
    print("-----------------------------------")
    print("Total Months: " + str(numMonths))
    print("Total: $" + str(netChange))
    print("Average Change: $" + str(netChange / numMonths))
    print("Greatest Increase in Profits: " + maxChangeDate + " ($" + str(maxChange) + ")")
    print("Greatest Decrease in Profits: " + minChangeDate + " ($" + str(minChange) + ")")
    
    file = open("analysis/results.txt", 'w')
    file.write("Financial Analysis\n")
    file.write("-----------------------------------\n")
    file.write("Total Months: " + str(numMonths))
    file.write("\nTotal: $" + str(netChange))
    file.write("\nAverage Change: $" + str(netChange / numMonths))
    file.write("\nGreatest Increase in Profits: " + maxChangeDate + " ($" + str(maxChange) + ")")
    file.write("\nGreatest Decrease in Profits: " + minChangeDate + " ($" + str(minChange) + ")")
    file.close()