#importing libraries
import os
import csv

#Importing csv file
budget_csv = os.path.join("election_data.csv")


# initialising variables
votes = 0

# opening the csv
with open(budget_csv, newline = "") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')
    
    # Skipping the header
    next(csv_reader)
    
    #looping through the csv
    for row in csv_reader:
        
        # Creating a dictionary on the first result
        if votes == 0:
            candidates = {row[2] : 1}
        
        # Add the new candidate if they are not in the dictionary
        else:
            if row[2] not in candidates:
                candidates[row[2]] = 1
            
            # If they are in the dictionary add one to the vote
            else:
                candidates[row[2]] += 1
                
        votes += 1

# Printing the results
print(f'Election Results')
print(f'------------------------')
print(f'Total Votes: {votes}')
print(f'------------------------')
for candidate, tally in candidates.items():
    print(f'{candidate}: {(tally/votes):.2%} ({tally})')
print(f'-----------------------')
print(f'Winner: {max(candidates, key = lambda x: candidates.get(x))}')
print(f'------------------------')

# Writing the results to a text file
text_file = open("Election_Results.txt","w")
text_file.write(f"Election Results\n")
text_file.write(f'------------------------\n')
text_file.write(f'Total Votes: {votes}\n')
text_file.write(f'------------------------\n')
for candidate, tally in candidates.items():
    text_file.write(f'{candidate}: {(tally/votes):.2%} ({tally})\n')
text_file.write(f'-----------------------\n')
text_file.write(f'Winner: {max(candidates, key = lambda x: candidates.get(x))}\n')
text_file.write(f'------------------------\n')
text_file.close()