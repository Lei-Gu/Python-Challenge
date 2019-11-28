import os
import csv

data_csv = os.path.join("Resources", "election_data.csv")

candidates = []
num_votes = []
percent_votes = []

total_votes = 0

# open file
with open(data_csv) as csvfile:

    reader = csv.reader(csvfile, delimiter = ',')

    header = next(csvfile) 

# sumup total_votes  
    for row in reader:
        
        total_votes += 1

# eliminate duplicate candidates and count the votes
        if row[2] not in candidates:

            candidates.append(row[2])

            index = candidates.index(row[2])

            num_votes.append(1)
        
        else:
            index = candidates.index(row[2])
            num_votes[index] += 1

# calculate and track percent  
    for votes in num_votes:
        percent_candidate = round((votes/total_votes)*100)
        percent_votes.append(percent_candidate)

# find most votes and locate winner
        winner = max(num_votes)
        index = num_votes.index(winner)
        winning_candidate = candidates[index]

# print results
print("Election Results")
print("..................................................")    
print(f"Total Votes: {str(total_votes)}")
print("..................................................")  
for i in range(len(candidates)):
    print(f"{candidates[i]} : {str(percent_votes[i])} % ({str(num_votes[i])})")
print("..................................................")  
print(f"Winner: {winning_candidate}")
print("..................................................")  

# export results into txt file
   
file = open("Results.txt","w")

file.write("Election Results" + "\n")

file.write("..............................................." + "\n")

file.write(f'Total Votes: {total_votes}' + "\n")

file.write("..............................................." + "\n")

for i in range(len(candidates)):

    file.write(f'{candidates[i]} : {percent_votes[i]} % ({num_votes[i]})' + "\n")

file.write("..............................................." + "\n")

file.write(f'Winner: {winning_candidate}' + "\n")

file.write("..............................................." + "\n")

file.close()