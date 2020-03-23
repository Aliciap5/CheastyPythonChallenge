#import modules
import os
import csv

# defile file
file= os.path.join("election_data.csv")

# Create the function
def analyze_election(file):

    #Declare variables and inital value
    voteCast= 0
    winner = ""
    canidatelst = []
    candidate = ""
    candidate0 = 0
    candidate1 = 0
    candidate2 = 0
    candidate3 = 0
    

    # Read the CSV file
    with open(file,"r") as data:
        csvreader = csv.reader(data, delimiter = ",")
        header = next(csvreader)
        
        # Create the for loop to read the cvs file
        for row in csvreader:        
            
            # The total number of votes cast
            voteCast += 1       
    
            # A complete list of candidates who received votes
            candidate = row[2]
            if candidate not in canidatelst:
                canidatelst.append(candidate)

            # The total number of votes each candidate won
            if candidate == canidatelst[0]:
                candidate0 += 1
            elif candidate == canidatelst[1]:
                candidate1 += 1
            elif candidate == canidatelst[2]:
                candidate2 += 1
            elif candidate == canidatelst[3]:
                candidate3 += 1
        
            # The percentage of votes each candidate won- calaculated in analysis statement

            # The winner number of total votes.
            winningTot = max(candidate0,candidate1,candidate2,candidate3)
            
            # The winner of the election based on popular vote.
            if winningTot == candidate0:
                winner = canidatelst[0]
            if winningTot == candidate1:
                winner = canidatelst[1]
            if winningTot == candidate2:
                winner = canidatelst[2]
            if winningTot == candidate3:
                winner = canidatelst[3]
        
        analysis = f"""
        Election Results
        -------------------------
        Total Votes: {voteCast}
        -------------------------
        {canidatelst[0]}: {round((candidate0/voteCast)*100)}% total votes: {candidate0}
        {canidatelst[1]}: {round((candidate1/voteCast)*100)}% total votes: {candidate1}
        {canidatelst[2]}: {round((candidate2/voteCast)*100)}% total votes: {candidate2}
        {canidatelst[3]}: {round((candidate3/voteCast)*100)}% total votes: {candidate3}
        -------------------------
        Winner: {winner}
        -------------------------
        """
        # Print results to the terminal
        print(analysis)

        # to create an output text file
        # Specify the file to write and create the text file
        output_file="output.txt"
        with open(output_file, "w") as doc:
            doc.write(analysis)

# Create file path for csv import
path = os.path.join("election_data.csv")
# Run the function on the path
analyze_election(path)