# python_Challenge

## Background
This repository brings a python solution for real-life situations. The situations encompass financial, election, human resources, and linguistic research data. The financial data sourced under [PyBank/Resources](PyBank/Resources/budget_data.csv) folder, the election data sourced under [PyPoll/Resources](PyPoll/Resources/) folder, the human resource data sourced under [ PyBoss/Resources](PyBoss/Resources/employee_data.csv) folder, and the research data sourced under [PyParagraph/Resources](PyParagraph/Resources) folder.

The code's organized to analyze the data, and create an output file in the Analysis subfolder in each project.


Note : All the main codes are set up to the relative path to be auto-adjusted in your working directory, however, the path in the video below is just my directory for demonstration.

For example the relative directories looks as follows:

 To import         `data_path=os.path.join('Resources', 'budget_data.csv')`
 
 To export Output  `output_file = os.path.join('Analysis', 'pyBank_output.txt')`

<!-- TABLE OF CONTENTS -->
## Table of Contents

* [PyBank](PyBank/)
  * [Resources](PyBank/Resources/budget_data.csv)
  * [Analysis output](PyBank/Analysis/pyBank_output.txt)
* [PyPoll](PyPoll/)
  * [Resources](PyPoll/Resources/)
  * [Analysis output](PyPoll/Analysis/pyPoll_output.txt)

## PyBank
In this challenge, a python script created to analyze the financial data of a company and give an output. The dataset [budget data](PyBank/Resources/budget_data.csv) is composed of two columns: `Date` and `Profit/Losses`.

 
The [main script](PyBank/main.py) analyzes, and create an output in PyBank [Analysis](PyBank/Analysis/pyBank_output.txt) sub-folder. 
 
 
 The code compute the following tasks:
 
  * The total number of months included in the dataset

  * The net total amount of "Profit/Losses" over the entire period

  * The average of the changes in "Profit/Losses" over the entire period

  * The greatest increase in profits (date and amount) over the entire period

  * The greatest decrease in losses (date and amount) over the entire period


 In this challenge, a python script created to modernize a vote-counting process of a small rural town. This script used [election dataset](PyPoll/Resources/), and it is composed of three columns: `Voter ID`, `County`, and `Candidate`.
 
 
 
The [main script](PyPoll/main.py) analyzes, and create an output in PyPoll [Analysis](PyPoll/Analysis/pyPoll_output.txt) sub-folder. 
 
 
 The code compute the following tasks:
 
  * The total number of votes cast

  * A complete list of candidates who received votes

  * The percentage of votes each candidate won

  * The total number of votes each candidate won

  * The winner of the election based on popular vote.
  

  
  Jordan Wright Washu dataviz 2021