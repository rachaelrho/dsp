#The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

# The below skeleton is optional.  You can use it or you can write the script with an approach of your choice.


#import csv
import pandas as pd

  def read_data(data):
    parsed_data = pd.read_csv(data)
    print parsed_data
  ##when i read in the data with a function i can't seem to call d (the data) afterwards. can you advise a different approach?


  def get_min_score_difference(parsed_data):
    parsed_data['absDiff'] = abs(parsed_data['Goals']-parsed_data['Goals Allowed'])
    minRow = parsed_data['absDiff'].argmin()
    print(parsed_data['Team'][minRow])
