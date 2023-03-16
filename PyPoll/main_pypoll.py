# main_pypoll.py
# Andrew Lounsbury
# 3/16/23
# Purpose: module 3 for Vanderbilt Data Analytics Bootcamp; processes data in given election_data.csv
import os, csv

csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    
    votes = [0, 0, 0]
    numVotes = 0
    for row in csvreader:
        numVotes += 1
        if row[2] == "Charles Casper Stockham":
            votes[0] += 1
        elif row[2] == "Diana DeGette":
            votes[1] += 1
        elif row[2] == "Raymon Anthony Doane":
            votes[2] += 1
        else:
            print("Error: extra candidate")
            
    percentage1 = votes[0] / numVotes * 100
    percentage2 = votes[1] / numVotes * 100
    percentage3 = votes[2] / numVotes * 100
    
    if votes[0] > votes[1] and votes[0] > votes[2]:
        winner = "Charles Casper Stockham"
    elif votes[1] > votes[0] and votes[1] > votes[2]:
        winner = "Diana DeGette"
    elif votes[2] > votes[0] and votes[2] > votes[1]:
        winner = "Raymon Anthony Doane"
    else:
        print("Error calculating winner")
    
    print("Election Results")
    print("--------------------------")
    print("Total Votes: " + str(numVotes))
    print("--------------------------")
    print("Charles Casper Stockham: " + str(round(percentage1, 3)) + "% (" + str(votes[0]) + ")")
    print("Diana DeGette: " + str(round(percentage2, 3)) + "% (" + str(votes[1]) + ")")
    print("Raymon Anthony Doane: "  + str(round(percentage3, 3)) + "% (" + str(votes[2]) + ")")
    print("--------------------------")
    print("Winner: " + winner)
    print("--------------------------")
    
    file = open("C:/Users/aloun/Desktop/Bootcamp/module 3/Instructions/python-challenge/PyPoll/analysis/results.txt", 'w')
    file.write("Election Results")
    file.write("\n--------------------------")
    file.write("\nTotal Votes: " + str(numVotes))
    file.write("\n--------------------------")
    file.write("\nCharles Casper Stockham: " + str(round(percentage1, 3)) + "% (" + str(votes[0]) + ")")
    file.write("\nDiana DeGette: " + str(round(percentage2, 3)) + "% (" + str(votes[1]) + ")")
    file.write("\nRaymon Anthony Doane: "  + str(round(percentage3, 3)) + "% (" + str(votes[2]) + ")")
    file.write("\n--------------------------")
    file.write("\nWinner: " + winner)
    file.write("\n--------------------------")