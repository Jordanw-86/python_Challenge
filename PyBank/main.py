import os
import csv

csvpath = os.path.join("..", "PyBank", "Resources", "budget_data.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    if csv.Sniffer().has_header:
        next(csvreader)

    print(csvreader)

## Loop through to create list

    Dates = []
    Profit_loss = []
    Changes = []
    Changesdate = []
    counter = 0
    netTotal = 0
    preValue = 0

    for row in csvreader:
        counter = counter + 1
        if counter > 1:
            changeDelta = int(row[1]) - preValue
            #print("change should be", changeDelta)
            Changesdate.append([changeDelta,row[0]])
            Changes.append(changeDelta)
        
            #print(Changes)
        netTotal = netTotal + int(row[1])
        prevvalue = int(row[1])
       # print(prevvalue)
    
    totalMonths = counter 
    sumChanges = float(sum(Changes))
    #print(sumChanges)
    lengthList = len(Changes)
    averageChange = float(sumChanges / lengthList)
    averageChange = round(averageChange,2)
    Changesdate.sort()
    lastNumber = Changesdate[len(Changes)- 1]
    firstNumber = Changesdate[0]

    print('Financial Analysis')
    print('--------------------\n')
    print('Total Months:', totalMonths)
    print('Total: $', netTotal)
    print('Average Change: $', averageChange)
    print('Greatest Increase:', lastNumber)
    print('Greatest Decrease:', firstNumber)

    f = open('Pybank.txt', 'w')
    f.write('Financial Analysis')
    f.write('--------------------\n')
    f.write('Total Months:')
    f.write('Average Change: $')
    f.write('Greatest Decrease:')
    f.close()
    #print(Changesdate)
    #print(lastNumber,firstNumber)
   # print(averageChange
    #print(lengthList)
    #print(sumChanges)
    #print(totalMonths) 
    #print(netTotal)
    #print(Changes)
    #print(listSort)
        

    





    

        