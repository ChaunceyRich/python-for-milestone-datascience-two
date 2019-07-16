#Question 4
#Import relevant libraries 
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
%matplotlib inline
#read data file
data = pd.read_csv("./Desktop/UCC/CAFires92.csv")
#group data for plotting 
fby = data.groupby("year")["fd_unq_id"].count()
