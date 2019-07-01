# python-for-milestone-datascience-two
Python for Sabree Datascience Science 2019

Please thoroughly read the instructions below.
When you are ready to take the Final Exam, please fork 
the project and make changes to the code and submit 
a pull request with your answers to each of the questions.

The total for all work is for 10 points

**Section 1: Commenting is important**

*Use Python Comments to Document Code and Functions (3 pts)*

Within code cells, be sure to also add Python comments to document each code block and use the PEP 8

guidelines to assign appropriate variable names that are short and concise but also clearly indicate the

kind of data contained in the variable.

Be sure to add documentation within your functions using Python comments to tell the user what the function

is doing and and what inputs it can take. Also, be sure to use clear function names that tell the user what

the function does. If you find it useful, you can review the PEP8 Style Guide.


**Section 2: Questions 1-4 Using Pandas Dataframes**

Data:

Get Data and read data into a data frame.

Use .urllib.request to download the following .csv file of fires in California and import the data to a pandas dataframe:

CA_fires_1992_2015_gt_100_acres.csv from https://ndownloader.figshare.com/files/12835340

The data contains one record for every fire greater than 100 acres that occurred between 1992 and 2015.
The dataset has columns for the size of the fire (acres) and for the year and month of the fire, along with other details about the cause, reporting agency, county name, etc.

*Question 1: Explore Structure of the Pandas Dataframe (1 pts)*

Use the appropriate functions to print the first few rows of the pandas dataframe and the last few rows of the dataframe.

Note: as this dataframe contains many records, it is not helpful to print the whole dataframe.


*Question 2: Summarize Fire Size (1 pts)*

Use the appropriate function to calculate summary statistics of only the fire size (acres).

Calculate the mean, minimum, and maximum fire size (acres) in this dataset.
Calculate the total number of fires in this dataset.


*Question 3: Calculate Total Number of Fires For Each Year (1 pts)*

Use the appropriate function to calculate the total number of fires per year, and save as a new dataframe.

Note: the displayed data below only shows the first few rows in the dataset.

Hints:

Review the use of groupby to run statistics on pandas dataframes.
Think about what value you want to use to group the data and what value you want to use to determine the total number of fires.

*Question 4: Plot Total Number of Fires For Each Year (1 pts)*

Create a plot of your choice (i.e. type, color) that displays the total number of fires for each year of data.

Be sure to label your x- and y-axes appropriately and give your plot an appropriate title.

Hint:

Think about which dataframe you want to use for the plot and what data you need to plot.

**Section 3: Questions 5-7 Using Numpy Arrays**

Get Data

Use .urllib.request to download the following .csv file of the number of fires by month and year in California and import the data to numpy arrays:

CA-fires-month-count-1992-to-2015.csv from https://ndownloader.figshare.com/files/12835346
The dataset contains a row for each year specified in the dataset name and contains a column for each month 

(starting with January through December). The values represent the number of fires that occurred in that month and year, 

based on fires greater than 100 acres that occurred between 1992 and 2015.

*Question 5: Write Function to Calculate Sum Across Columns (1 pts)*

Write a function that calculates the sum across columns of a numpy array.

*Question 6: Execute Function to Calculate Sum Across Columns (1 pts)*

Run the function created in the previous question (i.e. to calculate sum across columns in a numpy array) on the numpy array you created for CA-fires-month-count-1992-to-2015.csv. Save the output to a new numpy array.

*Question 7: Create Manual Numpy Array (1 pts)*

Manually create a numpy array that contains the month names for January to December and print the values in this new numpy array.

