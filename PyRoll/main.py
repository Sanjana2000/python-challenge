# import os module
import os

# import csv module
import csv

# Path to CSV file
csvpath = os.path.join('/Users/leahkrausetp/Desktop/Leah_UCB/PROJECTS/python-challenge/PyPoll','Resources', 'election_data.csv')

# Read CSV file in "read" mode. Assign readable file as a new variable
with open(csvpath) as csvfile:

# Specifies delimiter and variable. Prints this into csv reader
    csvreader = csv.reader(csvfile, delimiter=',')

# Read header and skips it
    header = next(csvreader)

# Create lists to store data
    voter_id = []
    candidate = []
    candidates_votes = []
    indv_candidates = []

# Create variables
    can1_votes = 0
    can2_votes = 0
    can3_votes = 0
    total_votes = 0

# Create a function that provides the total number and percentage each candidate received
    for row in csvreader:

# Total votes
        voter_id.append((row[0]))
# Candidate list
        candidate.append(row[2])

# Attain individual candidates names without repetition
    indv_candidates = list(set(candidate))

    with open(csvpath) as csvfile2:
        csvreader2 = csv.reader(csvfile2, delimiter=',')
        header = next(csvreader2)

        for row in csvreader2:
# Count up votes per candidate
            if row[2] == indv_candidates[0]:
                can1_votes += 1
            elif row[2] == indv_candidates[1]:
                can2_votes += 1
            elif row[2] == indv_candidates[2]:
                can3_votes += 1

# Calculate total number of votes
        total_votes = len(voter_id)

# Voter percentage per candidate
        can1_percentage = round(can1_votes / total_votes * 100, 3)
        can2_percentage = round(can2_votes / total_votes * 100, 3)
        can3_percentage = round(can3_votes / total_votes * 100, 3)

# Winner 
if can1_percentage > can2_percentage and can3_percentage:
    winner = indv_candidates[0]
elif can2_percentage > can3_percentage and can1_percentage:
    winner = indv_candidates[1]
elif can3_percentage > can2_percentage and can1_percentage:
    winner = indv_candidates[2]

#################################################################

# Print output
print("Election Results")
print("--"*15)
print("Total Votes: ", total_votes)
print("--"*15)
print(f"{indv_candidates[0]}: {can1_percentage}% ({can1_votes})")
print(f"{indv_candidates[1]}: {can2_percentage}% ({can2_votes})")
print(f"{indv_candidates[2]}: {can3_percentage}% ({can3_votes})")
print("--"*15)
print(f"Winner: {winner}")
print("--"*15)

# Print output to text file
with open ("PyPoll_Output.text", "w") as x:
    x.write("Election Results")
    x.write("\n")
    x.write("--"*15)
    x.write("\n")
    x.write(f"Total Votes: {total_votes}")
    x.write("\n")
    x.write("--"*15)
    x.write("\n")
    x.write(f"{indv_candidates[0]}: {can1_percentage}% ({can1_votes})")
    x.write("\n")
    x.write(f"{indv_candidates[1]}: {can2_percentage}% ({can2_votes})")
    x.write("\n")
    x.write(f"{indv_candidates[2]}: {can3_percentage}% ({can3_votes})")
    x.write("\n")
    x.write("--"*15)
    x.write("\n")
    x.write(f"Winner: {winner}")
    x.write("\n")
    x.write("--"*15)