# MY CODE PLAN FOR THE ELECTION ANALYSIS:

# The data we need to retrieve.
# 1. The total number of votes cast.
# 2. A complete list of candidates who received votes.
# 3. The percentage of votes each candidate won.
# 4. The total number of votes each candidate won.
# 5. The winner of the election based on popular vote. 
#-----------------------------------------------------------------------

# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to path.
file_to_save = os.path.join("Resources", "election_analysis.txt")
# 1. Ininialize a total vote counter
total_votes = 0
# Candidate options and candidates votes
candidate_options =[]
# 1. Declare the empty dictionnary
candidate_votes = {}
# Track the Winning candidate, vote count, and percecntage.
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read the header row.
    headers = next(file_reader)    
    # Print each row in the CSV file.

    for row in file_reader:
        # 2. Add to the total vote count.
        total_votes += 1
        # Get the canditate name from each row.
        candidate_name = row[2]
        # If the candidate does not match any existing candidate add it to the candidate list.
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidates list
            candidate_options.append(candidate_name)
            # 2. And Begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1
# Save the results to our text file
with open(file_to_save, "w") as txt_file:
    # print the final count to the terminal      
    election_results = ( 
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # save the final vote count to the text file.
    txt_file.write(election_results)
    for candidate_name in candidate_votes:
        # Retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]
        # 3 Calculate the percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        # Print each candidate's voter count and percentage to the terminal
        print(candidate_results)
        # Save the candidate results to our text file
        txt_file.write(candidate_results)           
        # Determine winning vote count, winning percentage, and candidate.        
        if (votes > winning_count) and (vote_percentage > winning_percentage):
                    # If true then set winning_count = votes and winning_percentage = vote_percentage
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
    # Print the winning candidates result to the terminal.
    winning_candidate_summary = (
        f"----------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage: .1f}%\n"
        f"----------------------------\n")
        
    print(winning_candidate_summary)
    # Save the winnig candidate's results to the text file
    txt_file.write(winning_candidate_summary)







    

        





    



   