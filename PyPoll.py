# The data we need to retrieve.
# 1. The total number of votes cast.
# 2. A complete list of candidates who received votes.
# 3. The percentage of votes each candidate won.
# 4. The total number of votes each candidate won.
# 5. The winner of the election based on popular vote. 

# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Ininialize a total vote counter
total_votes = 0
# Candidate options and candidates votes
candidate_options =[]
# 1. Declare the empty dictionnary
candidate_votes = {}
# Open the election results and read the file.
# Winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)    
    # Print each row in the CSV file.
    for row in file_reader:
        # 2. Add to the total vote count.
        total_votes += 1
        # print the canditate name from each row.
        candidate_name = row[2]
        
        # If the candidate does not match any existing candidate
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidates list
            candidate_options.append(candidate_name)
            # 2. Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0
         # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1
    # Determine the percentage of votes for eah candidate by looping through the counts
    # 1 Iterate throughtthe candidate list
    for candidate_name in candidate_votes:
        # 2 Retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]
        # 3 Calculate the percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100
        # To do: print out each candidate's name, vote count, and percentage of votes to the terminal
        # Determine winning vote count and candidate.
        # Determine if the votes is greater than the winning count.
        if (votes > winning_count) and (vote_percentage> winning_percentage):
                # If true then set winning_count = votes and winning_percentage = vote_percentage
                winning_count = votes
                winning_percentage = vote_percentage
                # And set the winning_candidate equal to the candidate's name
                winning_candidate = candidate_name
        # To do: Print out each candidate's name, vote count, and percentage of votes to the terminal
        print(f"{candidate_name}: {vote_percentage: .1f}% ({votes:,})\n")
    winning_candidate_summary = (
        f"----------------------------\n"
        f"winner: {winning_candidate}\n"
        f"winning vote count: {winning_count:,}\n"
        f"winning Percentage: {winning_percentage: .1f}%\n"
        f"----------------------------\n")
    print(winning_candidate_summary)






        #print(f"{candidate_name} : received {vote_percentage}% of the vote.")
# Print the candidate vote dictionary.
#print(candidate_votes)

    

        





    



   