# Create a Python script that analyzes the votes and calculates each of the following:
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.

# -------------------------------------------------------------

# Import dependencies
import os
import csv

number_votes = 0


# path to election_data and output file
pypoll_path_csv = os.path.join("Resources", "election_data.csv")
pypoll_output_csv = os.path.join("Output", "election_data.text")

# Define pypoll variables
candidates = []
votes_each_candidate = []


# open the file in "read" mode
with open(pypoll_path_csv) as pypoll_csvfile:
    csvreader = csv.reader(pypoll_csvfile, delimiter=",")
    # print(csvreader)
    csv_header = next(pypoll_csvfile)
    # print(f"csv_header:{csv_header}")
    for row in csvreader:
        # print(row)
        candidates.append(row[2])
        candidates_list = sorted(candidates)
        print(candidates_list)
    #     votes_each_candidate.append(candidates_list:row[1])
    # total_number_candidates = (candidates_list)
    # print(candidates_list)