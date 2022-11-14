# import the required modules
import os
import csv

# Create a path for the csv file
election_data_path = os.path.join('..', 'python-challenge', 'PyPoll', 'Resources', 'election_data.csv')

# Create path to make the analysis.txt file
analysis_path = os.path.join('..', 'python-challenge', 'PyPoll', 'analysis', 'analysis.txt')

# define a all the function I will need for the csv file
# Created a sum function to add up all the numbers in an array
def sum(arry):
    _sum = 0
    # This for loop runs throught the array for the number of items in the array
    # It then adds each number in the array together and returns the total
    for i in arry:
        _sum = _sum + i
    
    return(_sum)

# Created a mean function that uses the previously created sum function and divides
# by the length of the array
def mean(arr):
    mean_ = sum(arr)/len(arr)

    return(mean_)

#created a empty list that will be filled from the csv with the name of the candidate on each ballot
votes = []

# Open the election csv file
with open(election_data_path) as election_csv:
    csv_election_data = csv.reader(election_csv, delimiter = ',')
    
    # Remove the first line from the CSV file as it was a header
    budget_header = next(csv_election_data)
    
    # Create for loop to go through all the lines of the csv file
    # Append the ballot vote to the votes list - This will result in a list of all the name of the candidates voted for
    for row in csv_election_data:
        # print(row)
        votes.append(row[2])
    # print(votes)

# Create vote total by aquiring the lend of the the votes list
total_votes = len(votes)

# Created two lists one to hold the name of each candidate and the second to hold the number of votes for that candidate
candidate = []
candidate_votes = []

# For loop that will search through the votes list and append any candidates that are not in the candidate list
# Then it will add a 0 to the candidate_votes list to initialize a count under the same index for that candidate
for vote in votes:
    if vote not in candidate:
        candidate.append(str(vote))
        candidate_votes.append(0)
    
    # after the previous conditional (if statment) adds the counter
    # this for loop add +1 to the candidate that appears in the vote in votes for loop
    # this is done using the index of the candidate as the candidate and candidate_votes have the same index number
    for candi in candidate:
        if vote == candi:
            candidate_votes[candidate.index(candi)] +=1
            # print(candi)

#Now I print the results in the terminal
print(f'Election Results')
print(f'----------------------------------------')
print(f'Total Votes: {total_votes}')
print(f'----------------------------------------')

# A most votes variable is created to allow the code to tell which candidate (by index) got the most votes
most_votes = 0

# Create for loop to for through the Candidate_votes list and identify which candidate has the most votes
for great_v in candidate_votes:
    if great_v > most_votes:
        most_votes = great_v

# Created a for loop to print out the candidate and they percentatage of the total vote so that this code is more reuseable
# As the number of candidate might vary from election to election
for candi in range(len(candidate)):
    print(f'{candidate[candi]}: {round((candidate_votes[candi]/total_votes)*100, 3)}% ({candidate_votes[candi]})')

print(f'----------------------------------------')

# print(candidate_votes.index(most_votes))
print(f'Winner: {candidate[(candidate_votes.index(most_votes))]}')
print(f'----------------------------------------')

# Print the results into a text file useing the same methods as stated above
with open(analysis_path,'w') as analysis:
    print(f'Election Results', file=analysis)
    print(f'----------------------------------------', file=analysis)
    print(f'Total Votes: {total_votes}', file=analysis)
    print(f'----------------------------------------', file=analysis)
    for candi in range(len(candidate)):
        print(f'{candidate[candi]}: {round((candidate_votes[candi]/total_votes)*100, 3)}% ({candidate_votes[candi]})', file=analysis)\
    
    print(f'----------------------------------------', file=analysis)
    print(f'Winner: {candidate[(candidate_votes.index(most_votes))]}', file=analysis)
    print(f'----------------------------------------', file=analysis)