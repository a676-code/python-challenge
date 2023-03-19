# main.py
# Andrew Lounsbury
# 3/16/23
# Purpose: module 3 for Vanderbilt Data Analytics Bootcamp; processes data in the given election_data.csv file
import os, csv

# getting the path to election_data.csv
csvpath = os.path.join('Resources', 'election_data.csv')

# opening and reading election_data.csv
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # storing the header
    csv_header = next(csvreader)
    
    # list for counting votes for each candidate
    votes = [0, 0, 0]
    numVotes = 0
    # looping through the records, computing the total number of votes and the votes for each candidate
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
            
    # computing the percentage of votes for each candidate
    percentage1 = votes[0] / numVotes * 100
    percentage2 = votes[1] / numVotes * 100
    percentage3 = votes[2] / numVotes * 100
    
    # determining the winning candidate
    if votes[0] > votes[1] and votes[0] > votes[2]:
        winner = "Charles Casper Stockham"
    elif votes[1] > votes[0] and votes[1] > votes[2]:
        winner = "Diana DeGette"
    elif votes[2] > votes[0] and votes[2] > votes[1]:
        winner = "Raymon Anthony Doane"
    else:
        print("Error calculating winner")
    
    # printing the results
    print("\nElection Results")
    print("--------------------------")
    print("Total Votes: " + str(numVotes))
    print("--------------------------")
    print("Charles Casper Stockham: " + str(round(percentage1, 3)) + "% (" + str(votes[0]) + ")")
    print("Diana DeGette: " + str(round(percentage2, 3)) + "% (" + str(votes[1]) + ")")
    print("Raymon Anthony Doane: "  + str(round(percentage3, 3)) + "% (" + str(votes[2]) + ")")
    print("--------------------------")
    print("Winner: " + winner)
    print("--------------------------")

    # writing the results pypoll_results.txt
    file = open("analysis/pypoll_results.txt", 'w')
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