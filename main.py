import os
import csv

csvpath = os.path.join("..", "PyPoll", "Resources", "election_data.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    if csv.Sniffer().has_header:
        next(csvreader)

    

##List to loop throguh

    total_votes = []
    Candidates = []
    num_votes = 0
    

    for row in csvreader:
        #total number of votes
        num_votes = num_votes + 1

        #The candidate voted for
        # candidate is not list
        candidate = row[2]
        if candidate in Candidates:
            liar_position = Candidates.index(candidate) 
            total_votes[liar_position] = total_votes[liar_position] + 1
        
        else: 
            total_votes.append(1)
            Candidates.append(candidate)
    
            

    percent_of_votes = []
    #max_vote_Cast = total_votes[0]
    max_vote_index = 0
    vote_percentage = []

# this find the percentage of votes
    for i in total_votes:
        j = round(i/num_votes*100,4)
        percent_of_votes.append(j)

    

   
    #this finds the winner

    voteList = total_votes.index(max(total_votes))
    print(voteList)
    
    winner = Candidates[voteList]
    #print(winner)
    winningCount = 0 
    winningCadidate = ""  
    index = 0
    print('Election Results')
    print('---------------------\n')
    print('Total Votes:',num_votes)
    print('-----------------------\n')
    #possible for loop through candidates

    for candidate in Candidates: 
        if (Candidates.count(candidate) > winningCount):
             winningCount = Candidates.count(candidate)
             winningCadidate = candidate
        output = f'{candidate}: {percent_of_votes[index]}% ({Candidates.count(candidate)})\n'

        index = index + 1
        print(output)
    print('--------------------\n')
    print('Winner', winner)
    print('--------------------\n')

    f = open('PyPoll.txt', 'w')
    f.write('Election Results\n')
    f.write('--------------------\n')
    f.write('Total Votes:',total_votes)
    f.write('--------------------\n')
     #possible for loop through candidates
    f.write('--------------------\n')
    f.write("Winner:",winner)
    f.write('--------------------\n')
    f.close()




        


       

