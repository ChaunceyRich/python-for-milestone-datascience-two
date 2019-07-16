#Question 2
#Import Pandas Library 
import pandas as pd 
#read data file
data = pd.read_csv("./Desktop/UCC/CAFires92.csv")
#Isolate Fire Size variable by creating dataframe
data["fire_size"]
#Summarize Fire size, includes Mean, Median and Maxium
data["fire_size"].describe()
#Calculate total number of fires by Unique ID
data["fd_unq_id"].count()
