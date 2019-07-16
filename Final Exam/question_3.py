
#Question 3
#Import Pandas Library 
import pandas as pd 
#read data file
data = pd.read_csv("./Desktop/UCC/CAFires92.csv")
#group year with unique id to get total number of unique fires per year
data.groupby("year")["fd_unq_id"].count()
