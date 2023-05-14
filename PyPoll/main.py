import pandas as pd

#set the path of the file and read using panda
url ='https://raw.githubusercontent.com/rafedmahbub/python-challenge/main/PyPoll/Resources/election_data.csv'
file = pd.read_csv(url, index_col=0)
output_txt = 'https://raw.githubusercontent.com/rafedmahbub/python-challenge/main/PyPoll/analysis/output.txt'

#print length and sum
print("Election Results")
print ("----------------------")
Total_Vote = len(file)
print(f"Total Votes: {Total_Vote}")
print ("----------------------")

#print unique candicate list
#print(file.Candidate.unique())

#Count how many votes each candidate got
Vote_perCandidate = file.groupby('Candidate').count()

#Count the percentage of votes for each candidate
Vote_Percentage = (Vote_perCandidate/Total_Vote)*100

#Add two dataframes togeter for printing
Vote_Result = pd.concat([Vote_Percentage,Vote_perCandidate], axis=1)
Vote_Result.rename(columns={'County':''}, inplace=True)
print(Vote_Result)
print ("----------------------")

#find the maximum vole winner and print name
Vote_Winner = Vote_perCandidate.loc[Vote_perCandidate['County'].idxmax()]
print(f"Winner is : {Vote_Winner.name}")
print ("----------------------")


#save output in Data Frame
df = pd.DataFrame({"Election Results":["Total Votes:","Vote Results:","Winner:"],
                   "Value": [Total_Vote,Vote_Result,Vote_Winner.name]})

#write Data Frame output as txt
#'C:/Users/rafed.mahbub/Documents/MyDoc/MyDoc/UBHM/Py/Assignment/python-challenge/PyPoll/analysis/output.txt'
with open(r'output.txt', 'a') as f:
    df_string = df.to_string(header=True, index=False)
    f.write(df_string)
    f.close()