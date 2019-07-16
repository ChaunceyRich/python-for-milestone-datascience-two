#Question 1
#Import Pandas Library 
import pandas as pd 
#read data file
data = pd.read_csv("./Desktop/UCC/CAFires92.csv")
#open data file for review
data
#print first 5 line for data to ensure data is correct
data.head()
#print last 5 lines
data.tail()
