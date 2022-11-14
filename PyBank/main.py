# import the required modules
import os
import csv

# Path for the csv file
budget_data_path = os.path.join('..', "python-challenge", 'PyBank', 'Resources', 'budget_data.csv')

# Path for analysis.txt file
analysis_path = os.path.join('..', "python-challenge", 'PyBank', 'Analysis', 'analysis.txt')

# Function creation for the csv file
# Created a sum function to add up all the numbers in an array

def sum(arry):
    _sum = 0
    # This for loop runs throught the array for the number of items in the array
    # It then adds each number in the array together and returns the total
    for i in arry:
        _sum = _sum + i
    
    return(_sum)

# Mean function that uses the previously created sum function and divides by the length of the array
def mean(arr):
    mean_ = sum(arr)/len(arr)

    return(mean_)

# Created a function that creates a list that is composed of the difference in the inputed array
def Diff_array(arra):
    # The list of difference in the numbers of the inputed array
    dif=[]
    # this for loop searches through the inputed array and appends the difference
    for i in range(len(arra)-1):
        dif.append(arra[i+1] - arra[i])
    return dif

# Created two list on of the profits and the dates
Profit_list = []
Date_list=[]

# Open the budget data csv file
with open(budget_data_path) as budget_csv:

    csv_budget_data = csv.reader(budget_csv, delimiter=',')

    # remove the header
    budget_header = next(csv_budget_data)
    # print(budget_header)

    # Create for loop to go through all the lines of the csv file and append the Profits/losses and dates to the appropriate list
    for row in csv_budget_data:
        
        Profit_list.append(float(row[1]))
        Date_list.append(row[0])
    
        # print(float(row[1]))

# Summing the Profit list will give the Total profit or losses
TotalProfit = sum(Profit_list)

# Create the list of difference of the Profit_list using the previously decribe function
Profit_diff = Diff_array(Profit_list)

# Create the mean of the difference in the profit list using the mean function
Mean_profit_change = mean(Profit_diff)


# Print out the results of the analysis

# print(month_count)
print(f'Financial Analysis')
print('----------------------------------------')
print(f'Total Months: {len(Profit_list)}')
print(f'Total: ${int(TotalProfit)}')
print(f'Average Change: ${round(Mean_profit_change,2)}')

# This find the index of the month with the most and least change in profit
max_mon = (Profit_diff.index(max(Profit_diff)))+1
min_mon = (Profit_diff.index(min(Profit_diff)))+1


print(f'Greatest Increase in Profits: {Date_list[max_mon]} (${int(max(Profit_diff))})')
print(f'Greatest Decrease in Profits: {Date_list[min_mon]} (${int(min(Profit_diff))})')

# Write out the analysis txt file
with open(analysis_path,'w') as analysis:
    print(f'Financial Analysis', file=analysis)
    print('----------------------------------------',  file=analysis)
    print(f'Total Months: {len(Profit_list)}', file=analysis)
    print(f'Total: ${int(TotalProfit)}',  file=analysis)
    print(f'Average Change: ${round(Mean_profit_change,2)}', file=analysis)
    print(f'Greatest Increase in Profits: {Date_list[max_mon]} (${int(max(Profit_diff))})', file=analysis)
    print(f'Greatest Decrease in Profits: {Date_list[min_mon]} (${int(min(Profit_diff))})', file=analysis)