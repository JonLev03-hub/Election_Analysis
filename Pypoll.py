#Goals of this code 1. count total votes 2. count votes per candidate 3. count % vote per candidate 4. calculate winner based on popular vote
#
# innitialize a dictionary for candidates votes
#
# for every row
#   -if candidate is in the dictionary add a vote to them 
#   -else add them to the dictionary and give them one vote 
#
# print total votes, print votes per candidate and % per candidate in the same line,
# print key with largest value 

#All nessicary imports 
import datetime as dt , csv, os

#create a current time variable
start = dt.datetime.now()

# create a dictionary to hold votes
Candidates = {}

#opening the CSV data and reading the CSV
fileToLoad = "election_results.csv"
with open(fileToLoad) as file :
    fileReader = csv.reader(file)
    next(fileReader, None) #Skips first line
    previous = ""
# Records total votes per person
    for row in fileReader : 
        if row[2] == previous :
            Candidates[row[2]] += 1
        else :
            Candidates.update({row[2] : 1})
            previous = row[2]
    
# Opening the save file
fileToSave = os.path.join("Analysis","Results.txt")
with open(fileToSave, "w") as file :
    file.write("Counties in the election\n------------------------\nArapahoe\nDenver\nJefferson")
# Counts Total Votes
# Counts Individual Vote %
# Writes Winner

