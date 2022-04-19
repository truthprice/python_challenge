# Import dependencies for reading the csv file and counting the votes
import os
import csv
from collections import Counter 

# Retrieve the csv file
election_csv = os.path.join("Resources", "election_data.csv")

# Create an empty list to store all candidate name occurrences 
candidate = []

# Create a variable to store the vote total
total_votes = 0

# Read the csv file and designate the header
with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    # Loop through the candidate names in the file
    for row in csvreader:

        # Append names of candidates to a list
        candidate.append(row[2])
        # Count the total votes 
        total_votes +=1
        
    # Create a dictionary with each candidate's name and their vote total by counting the number of occurrences of each candidate name
    candidate_totals = dict(Counter(candidate))

    # Create a variable for calculating the winning vote total
    winning_total = 0

    # Loop through the dictionary to find the winning candidate
    for name, vote in candidate_totals.items():
      if vote > winning_total:
        winner = name
        winning_total = vote

# Create a string to print the results (including calculating the vote percentage for each candidate)
Election_Results = f'''
  Election Results
  ----------------------------
  Total Votes: {total_votes}
  ----------------------------
  Charles Casper Stockham: {(candidate_totals['Charles Casper Stockham']/total_votes) * 100:.3f}% ({candidate_totals['Charles Casper Stockham']})
  Diana DeGette: {(candidate_totals['Diana DeGette']/total_votes) * 100:.3f}% ({candidate_totals['Diana DeGette']})
  Raymon Anthony Doane: {(candidate_totals['Raymon Anthony Doane']/total_votes) * 100:.3f}% ({candidate_totals['Raymon Anthony Doane']})
  ----------------------------
  Winner: {winner}
  ----------------------------
'''
print(Election_Results)

# Export the report to a text file
with open("Analysis/election_data.txt", "w") as Election_Analysis: 
    Election_Analysis.write(Election_Results)