# In this Challenge, you are tasked with helping a small, rural U.S. town modernise its vote-counting process.
# You will be given a set of poll data called  election_data.csv . 
# The dataset is composed of three columns: "Voter ID", "County", and "Candidate". 
# Your task is to create a Python script that analyzes the votes and calculates each of the following values:
# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote

#Importing the necessary modules/libraries
import os
import csv

# Set path
election_data_csv = os.path.join('e:/UWA_BootCamp/python-challenge/PyPoll','Resources', 'election_data.csv')

# Open and read CSV File
with open (election_data_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # Reading the header row
    header = next(csvreader)

    # Set variables
    total_votes = 0
    votes_per_candidate = {}


    # The total number of votes cast
    # A complete list of candidates who received votes
    for row in csvreader:
    # count total votes
        total_votes += 1

        # count votes per candidate
        # check if candidate is in dictionary votes_per_candidate
        if row[2] not in votes_per_candidate:
        
        # if not found, execute this and create new entry in the dictionary
            votes_per_candidate[row[2]] = 1
        else:
            # if candidate is already in the dictionary, then execute this code
            # and count additional vote for this candidate
            votes_per_candidate[row[2]] += 1

# Displaying the above information
print("Election Result")
print("-----------------------------")
print("Total Votes: " + str(total_votes))
print("-----------------------------")

# The total number of votes each candidate won
# The percentage of votes each candidate won
# Loop through each candidate and their votes
# Print the candidate name, percentage of their votes in three decimals
for candidate, votes in votes_per_candidate.items():
    print(candidate + ": " "{:.3%}".format(votes/total_votes)+" ("+str(votes)+")")
    print("-----------------------------")
    

# The winner of the election based on popular vote
winner = max(votes_per_candidate, key=votes_per_candidate.get)
print(f"Winner:{winner}")
print("-----------------------------")

# Exporting the result to .txt file
output = open("Pypoll Output.txt", "w")

output.write("Election Result\n")
output.write("-----------------------------\n")
output.write(f"Total Votes: + str(total_votes)\n")
output.write("-----------------------------\n")
output.write(candidate + ": " "{:.3%}".format(votes/total_votes)+" ("+str(votes) +")\n")
output.write("-----------------------------\n")
output.write(f"Winner:{winner}\n")
output.write("-----------------------------\n")

