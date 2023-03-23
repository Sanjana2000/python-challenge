# python-challenge

## PyBank

This code analyzes the financial data located in budget_data.csv. The dataset is composed of two columns: "Date" and "Profit/Losses".

First, import the OS and CSV modules

Set the path to the correlating CSV file

Identify any variables as strings, integers, or lists as necessary

Read in CSV file, set it as a variable and specify the delimiter

Read in header and skip it

Keep track of variables that you will need to evaluate by looping through rows

Calculate the average change from month to month

Print output

Export output to text file

Your analysis should look similar to the following:

Financial Analysis
----------------------------
Total Months: 86
Total: $22564198
Average Change: $-8311.11
Greatest Increase in Profits: Aug-16 ($1862002)
Greatest Decrease in Profits: Feb-14 ($-1825558)



## PyPoll

This code analyzes the votes and calculates results from data called election_data.csv. The dataset is composed of three columns: "Voter ID", "County", and "Candidate".

First, import the OS and CSV module

Set the path to the correlating CSV file

Read in CSV file, set it as a variable and specify the delimiter

Read in header and skip it

Identify any variables as strings, integers, or lists as necessary

Loop through rows and total up the total votes and the list of candidates that recieved votes

Attain a list of unique candidates excluding repetition

Loop through rows to count up the votes for each candidate

Calculate the total number of votes by the length of the list of all votes

Calculate the percentage of votes each candidate received

Identify the winner by the percentage of votes they won

Print output

Export output to text file

Your analysis should look similar to the following:

Election Results
-------------------------
Total Votes: 369711

Charles Casper Stockham: 23.049% (85213). 
Diana DeGette: 73.812% (272892). 
Raymon Anthony Doane: 3.139% (11606). 


Winner: Diana DeGette
