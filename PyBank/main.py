import os
import csv
import pandas as pd

#set the path of the file and read using panda
url ='https://raw.githubusercontent.com/rafedmahbub/python-challenge/main/PyBank/Resources/budget_data.csv'
file = pd.read_csv(url, index_col=0)
output_txt = 'https://raw.githubusercontent.com/rafedmahbub/python-challenge/main/PyBank/analysis/output.txt'

#print length and sum
print("Financial Analysis")
print ("----------------------")
Count = len(file)
print(f"Total Months: {Count}")
Total_Amount = file['Profit/Losses'].sum()
print(f"Total: ${Total_Amount}")


#Set variables
previous_profitloss = 0
profitloss_change = 0
profitloss_change_list = []
profitloss_average = 0
month_change = []
greatest_decrease = ["", 9999999]
greatest_increase = ["", 0]


#Loop through to find average profit/losses change and find greatest increase/decrease
for i,row in file.iterrows():
    profitloss_change = float(row['Profit/Losses']) - previous_profitloss
    previous_profitloss = float(row['Profit/Losses'])
    profitloss_change_list = profitloss_change_list + [profitloss_change]
    month_change = month_change + [i]

    if profitloss_change>greatest_increase[1]:
        greatest_increase[0]=i
        greatest_increase[1]=profitloss_change

    if profitloss_change<greatest_decrease[1]:
        greatest_decrease[0]=i
        greatest_decrease[1]=profitloss_change


profitloss_average_temp = sum(profitloss_change_list)/len(profitloss_change_list)
profitloss_average = round(profitloss_average_temp,2)
print(f"Average change: ${profitloss_average}")
print(f"Greatest Increase in Profits:{greatest_increase}")
print(f"Greatest Decrease in Profits: {greatest_decrease}")


#save output in Data Frame
df = pd.DataFrame({"Financial Analysis":["Total Months:","Total Revenue:","Average Revenue Change:","Greatest Increase in Profits:","Greatest Decrease in Profits:"],
                   "Value": [Count,Total_Amount,profitloss_average,greatest_increase,greatest_decrease]})

#write Data Frame output as txt
#'C:/Users/rafed.mahbub/Documents/MyDoc/MyDoc/UBHM/Py/Assignment/python-challenge/PyBank/output.txt'
with open(r'output_txt', 'a') as f:
    df_string = df.to_string(header=True, index=False)
    f.write(df_string)
    f.close()