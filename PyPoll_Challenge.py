import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#  Initialize.
total_votes = 0
candidate_options = []
candidate_votes = {}
counties = []
counties_dict = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# County name with largest voter turn out
county_voter = ""
vote_count = 0
highest_percentage = 0
# Open the election results and read the file
with open(file_to_load) as election_data:

     # To do: read and analyze data here.
     # Read the file object with the reader function.
     file_reader = csv.reader(election_data)

     # Read and print the header row.
     headers = next(file_reader)

     # Print each row in the CSV file.
     for row in file_reader:
         # 2. Add to the total vote count.
         total_votes += 1 

         # Print the candidate name from each row.
         candidate_name = row[2]

         # Print the county name from each row
         county_name = row[1]

         # If the candidate does not match any existing candidate...
         if candidate_name not in candidate_options:
             # Add it to the list of candidates.
             candidate_options.append(candidate_name)
         # 2. Begin tracking that candidate's vote count. 
             candidate_votes[candidate_name] = 0


         # Add a vote to that candidate's count.
         candidate_votes[candidate_name] += 1
       
         # If county name does not match existing county name
         if county_name not in counties:
             counties.append(county_name)
             counties_dict[county_name] = 0
         counties_dict[county_name] += 1
 
         # Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)

    for county in counties_dict:
        cvotes = counties_dict[county]

        cvote_percentage = float(cvotes) / float(total_votes) * 100
        #Print county name and percentage of the votes
        county_results = (
            f"{county}: {cvote_percentage: .1f}% ({cvotes:,})\n")
        print(county_results)
        txt_file.write(county_results) 

        if (cvotes > vote_count) and (cvote_percentage > highest_percentage):
            vote_count - cvotes
            highest_percentage = cvote_percentage
            county_voter = county
    highest_county_summary = (
        f"-----------------------\n"
        f"Largest County Turnout: {county_voter}\n"
        f"-----------------------\n")
    print(highest_county_summary)
    txt_file.write(highest_county_summary)

# 1. Iterate through the candidate list.
    for candidate in candidate_votes:
    # 2. Retrieve vote count of a candidate.
        votes = candidate_votes[candidate]
    # 3. Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
    # 4. Print the candidate name and percentage of votes.
        candidate_results = (
            f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

   # print(f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
        if (votes > winning_count) and (vote_percentage > winning_percentage):
         # If true then set winning_count = votes and winning_percent =
         # vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
         # And, set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate

    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)
