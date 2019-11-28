import os
import csv

data_csv = os.path.join("Resources", "budget_data.csv")

profits = []
months = []
profit_changes = []

# open file
with open(data_csv) as csvfile:

    reader = csv.reader(csvfile, delimiter = ',')

    header = next(csvfile) 

    print(f"Header: {header}")

# add values to months and profits 
    for row in reader:
        
        months.append(row[0])
        profits.append(int(row[1]))
    
# track profit changes into list and find max, min and average
    for i in range(1, len(profits)):

        profit_changes.append(int(profits[i])-int(profits[i-1]))
        
        avg_changes = sum(profit_changes)/ len (profit_changes)

        max_profit_change = max(profit_changes)
        min_profit_change = min(profit_changes)

# locate the max increase and max decrease

        greatest_increase_date = months[profit_changes.index(max(profit_changes))+1]

        greatest_decrease_date = months[profit_changes.index(min(profit_changes))+1]


        print("Financial Analysis")
        print("..................................................")    
        print(f"Total Months: {len(months)}")
        print(f"Total : {sum(profits)}")
        print(f"Average  Change: {avg_changes}")
        print(f"Greatest Increase in Profits: {str(greatest_increase_date)} '({max_profit_change})'")
        print(f"Greatest Decrease in Profits: {str(greatest_decrease_date)} '({min_profit_change})'")

 # export summary into txt file
   
    file = open("Summary.txt","w")

    file.write("Financial Analysis" + "\n")

    file.write("...................................................................................." + "\n")

    file.write("Total Months: " + str(len(months)) + "\n")

    file.write("Total: " + "$" + str(sum(profits)) + "\n")

    file.write("Average Change: " + "$" + str(avg_changes) + "\n")

    file.write("Greatest Increase in Profits: " + str(greatest_increase_date) + " " + "$" + str(max_profit_change) + "\n")

    file.write("Greatest Decrease in Profits: " + str(greatest_decrease_date) + " " + "$" + str(min_profit_change) + "\n")

    file.close()