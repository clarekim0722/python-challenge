import os
import csv

# Initialize variables and data structures
total_votes = 0
candidates = {}

# Read the CSV file
with open("election_data.csv", "r") as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)  # Skip the header row

    for row in csvreader:
        voter_id, county, candidate = row
        total_votes += 1
        
        # Count the votes for each candidate
        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1

#Get a List of Candidates who received votes
candidate_list = list(candidates.keys())

#Calculate the Percentage of Votes each Candidate won
percentages = {candidate: (votes / total_votes) * 100 for candidate, votes in candidates.items()}

#Determine the Winner
winner = max(candidates, key=candidates.get)

#Print the results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate in candidate_list:
    print(f"{candidate}: {percentages[candidate]:.3f}% ({candidates[candidate]})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")
