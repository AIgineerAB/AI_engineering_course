# Exercise 0 - pandas repetition

In this exercise, you get to repeat pandas and matplotlib as these are cruicial for working with data.

## 0. Car sales in Norway - emissions and trends

Go to [kaggle and download this dataset](https://www.kaggle.com/datasets/dmi3kno/newcarsalesnorway/data). In this exercise we'll work with `norway_new_car_sales_by_month.csv`

&nbsp; a) Do some EDA with info, find out column names, shape of dataset, describe method to get summary descriptive statistics.

&nbsp; b) Draw a line chart of quantity for each year. Is there a year that should be skipped?

&nbsp; c) Draw a line chart of average CO2 emissions for same years that as in b)

&nbsp; d) Draw a line chart of all years and months for import

&nbsp; e) Draw a line chart of all years and months for average CO2 emissions

&nbsp; f) Draw a line chart of all years and months for electric cars import where it's relevant.

&nbsp; g) Draw a line chart of average diesel share per year

&nbsp; h) Discuss some findings with a friend based on this dataset, and do plot more graphs

## 1. Salaries in data field

Go to [kaggle and download this dataset on job salaries in the data field](https://www.kaggle.com/datasets/adilshamim8/salaries-for-data-science-jobs). In this exercise it is many cases easier to solve the exercises if you combine duckdb with pandas for analysis.

&nbsp; a) Start with some simple EDA, check summary statistics, info, columns etc

&nbsp; b) Plot the distribution of the salaries in USD.

&nbsp; c) How many job postings are there for each job title? Take the tenth most common job title and plot a bar chart of the number of job postings for that title.

&nbsp; d) Create a dataframe that contains the following columns: job_title, experience_level, median_salary_usd, mean_salary_usd, mean_salary_sek. Sort the dataframe by mean_salary_sek.

&nbsp; f) Create a column with salary in SEK per month and make the distribution of salaries in SEK per month for all job postings

&nbsp; g) Now create distributions of monthly SEK based on different experience levels, do you see any trends?

&nbsp; h) Find median monthly swedish salary for more common job_titles. Think what common may mean here.

&nbsp; i) Join the country_codes.csv to the dataset get the actual country names. Find the median monthly salary in SEK for each country and the number of job postings.

## 2. Theory questions

&nbsp; a) Why could it be good to combine duckdb and pandas?

&nbsp; b) How do you create a DataFrame in Pandas from a dictionary, a list of dictionaries, and a CSV file, json object?

&nbsp; c) What is the difference between .loc[] and .iloc[] for indexing in Pandas?

&nbsp; d) What is the purpose of the .groupby() method in Pandas? How is it used in data aggregation?

&nbsp; e) How do you export a pandas dataframe into a csv file?

&nbsp; f) How do you save a pandas dataframe into a duckdb database?

## Glossary

Fill in this table either by copying this into your own markdown file or copy it into a spreadsheet if you feel that is easier to work with.

| terminology           | explanation |
| --------------------- | ----------- |
| dataframe             |             |
| series                |             |
| pandas concat         |             |
| pandas appply         |             |
| csv                   |             |
| pandas isnull         |             |
| masking in pandas     |             |
| pandas transpose      |             |
| pandas value_counts() |             |
| json                  |             |
| tabular data          |             |
| zero-based indexing   |             |
| join                  |             |
| left join             |             |
| inner join            |             |
| group by              |             |
|                       |             |
