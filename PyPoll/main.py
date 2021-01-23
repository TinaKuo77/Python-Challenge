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

# Define pypoll variables
candidates_list = []
candidate_name = []
votes_each_candidate = []
percentage_vote = []
number_votes = 0

# open the file in "read" mode
with open(pypoll_path_csv) as pypoll_csvfile:
    csvreader = csv.reader(pypoll_csvfile, delimiter=",")
    # print(csvreader)
    csv_header = next(csvreader)
    # print(f"csv_header:{csv_header}")

    # count total number of votes cast
    for row in csvreader:
        number_votes = number_votes + 1
        candidates_list.append(row[2])
        candidates_list = sorted(candidates_list)
        # print(number_votes)
        
    for candidate in set(candidates_list):
        candidate_name.append(candidate[0])
        number_candidates = candidates_list.count(candidate[0])
        votes_each_candidate.append(number_candidates)
        # print(votes_each_candidate)
        percentage_total_votes = (votes_each_candidate/number_candidates)*100
        percentage_vote.append(percentage_total_votes)
    votes_candidate_win = max(votes_each_candidate)
    winner_candidate = candidate_name[votes_each_candidate.index(votes_candidate_win)]

# print the analysis to the terminal
print("-------------------------")
print("Election Results")   
print("-------------------------")
print("Total Votes :" + str(number_votes))    
print("-------------------------")
for i in range(len(candidate_name)):
            print(candidate_name[i] + ": " + str(percentage_vote[i]) +"% (" + str(votes_each_candidate[i])+ ")")
print("-------------------------")
print("The winner is: " + winner_candidate)
print("-------------------------")

# Export a text file
pypoll_output_csv = os.path.join("Output", "election_data.text")
with open(pypoll_output_csv, "w") as text_file:
            text_file.writerow(
                f"----------------------------\n"
                f"Election Results\n"
                f"----------------------------\n"
                f"Total Votes : + str(number_votes)\n" 
                f"----------------------------\n"
                or i in range(len(candidate_name)):
                        print(candidate_name[i] + ": " + str(percentage_vote[i]) +"% (" + str(votes_each_candidate[i])+ ")")
                f"----------------------------\n"
                f"("The winner is: " + winner_candidate)\n"
                f"----------------------------\n"
            )
