import os
import csv

election_csv = os.path.join( 'Resources', 'election_data.csv')
election_output_file = "analysis/election_analysis.txt"


total_votes = 0
candidates = {}  # A dictionary to store candidate names as keys and their vote count as values

with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)  # Read the CSV header

    for row in csvreader:
        # Assuming candidate names are in the third column (adjust the index if needed)
        candidate_name = row[2]
        total_votes += 1

        # Update the vote count for the candidate
        if candidate_name in candidates:
            candidates[candidate_name] += 1
        else:
            candidates[candidate_name] = 1

# Determine the winner
winner = max(candidates, key=candidates.get)

# Calculate the percentage of votes each candidate won
percentage_votes = {candidate: (votes / total_votes) * 100 for candidate, votes in candidates.items()}

# Generate the election analysis report
election_analysis = (
    "Election Results\n"
    "-------------------------\n"
    f"Total Votes: {total_votes}\n"
    "-------------------------\n"
)

for candidate, votes in candidates.items():
    election_analysis += f"{candidate}: {percentage_votes[candidate]:.3f}% ({votes})\n"

election_analysis += "-------------------------\n"
election_analysis += f"Winner: {winner}\n"
election_analysis += "-------------------------\n"

# Print the analysis to the terminal
print(election_analysis)

# Export the analysis to a text file
with open(election_output_file, "w") as textfile:
    textfile.write(election_analysis)

print("Election analysis saved to 'election_analysis.txt'.")
