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

# path to election_data and output file
pypoll_path_csv = os.path.join("Resources", "election_data.csv")
pypoll_output_csv = os.path.join("Output", "election_data.text")

# Create a list
candidates_list = []
candidate_name = []
votes_each_candidate = []
percentage_vote = []

# Define pypoll variables
vote_count = 0

# open the file in "read" mode
with open(pypoll_path_csv) as pypoll_csvfile:
    csvreader = csv.reader(pypoll_csvfile, delimiter=",")
    # print(csvreader)
    # Read the header row
    csv_header = next(csvreader)
    # print(f"csv_header:{csv_header}")

    # count total number of votes cast
    for row in csvreader:
        vote_count = vote_count + 1
        candidates_list.append(row[2])
        # print(vote_count)
        
    for candidate in set(candidates_list):
        candidate_name.append(candidate)
        vote = candidates_list.count(candidate)
        votes_each_candidate.append(vote)
        # print(votes_each_candidate)
        percentage_total_votes = format((vote/vote_count)*100/(sum(vote.value())),".3f") 
        percentage_vote.append(percentage_total_votes)

    votes_candidate_win = max(votes_each_candidate)
    winner_candidate = candidate_name[votes_each_candidate.index(votes_candidate_win)]

# print the analysis to the terminal
print("-------------------------")
print("Election Results")   
print("-------------------------")
print("Total Votes :" + str(vote_count))    
print("-------------------------")
for i in range(len(candidate_name)):
            print(candidate_name[i] + ": " + str(percentage_vote[i]) +"% (" + str(votes_each_candidate[i])+ ")")
print("-------------------------")
print("Winner: " + winner_candidate)
print("-------------------------")

# # Export a text file
# pypoll_output_csv = os.path.join("Output", "election_data.text")
# with open(pypoll_output_csv, "w") as text_file:
#             text_file.writerow(
#                 f"----------------------------\n"
#                 f"Election Results\n"
#                 f"----------------------------\n"
#                 f"Total Votes : + str(vote_count)\n" 
#                 f"----------------------------\n"
#                 for i in range(len(candidate_name))
#                         print(candidate_name[i] + ": " + str(percentage_vote[i]) +"% (" + str(votes_each_candidate[i])+ ")")
#                 f"----------------------------\n"
#                 f"("The winner is: " + winner_candidate)\n"
#                 f"----------------------------\n"
#             )
