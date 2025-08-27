# Exercise 3 - pydantic

In this exercise, you get to work with data validation using pydantic v2

## NOT DONE YET

## 0. Pydantic warmup

This exercise will give you a feel of the pydantic library for data validation. 

a) Create a BaseModel for a User. It should have a required id (integer) and a required name (string). Instantiate the model with valid data and then with invalid data (e.g., a string for id) to see the ValidationError.

b) Create a BaseModel for a Person with the fields name, age, email, favourite pet. Add appropriate validation in each fields. Tips: you can use built-in EmailStr type in pydantic for validating email. Try out your Person class by instantiating it with different types of values for the fields to see proper validations. 

c) Use normal python class to replicate what you have created in b), i.e. create a Person class with proper input validation. 

d) 


## 1. Simulate a small company 

a) Connect python to gemini, very important that you place the api key in .env and gitignore it 

b) Use gemini to simulate 100 data points in json format containing the following fields: first_name, last_name, phone_number, email, department, salary, title. See if you can prompt to direct the LLM output to have swedish names, phone numbers in swedish format (+46 731 29 52), departments (IT, HR, marketing, sales), reasonable salary (you might need to check some swedish statistics on salaries) and corresponding titles within these departments. 

c) Now use pydantic to validate this json and put in proper schema that the fields should follow 

d) Write this json data to a folder called output_data 

e) Use pandas to read the data as dataframe

f) Write a csv file to your output_data

g) Use python to create a duckdb database with a staging layer and store this into a table called small_company. 

h) Use gemini to simulate departments data. There should be same departments as those you had in b). Also add a description field and a contact person. 

i) Add a departments table in your duckdb database under staging layer to store this data. 


## 1.

a)

b)

c)

d)

e)

f)

## 2. Theory questions

a)

b)

c)

## Glossary

Fill in this table either by copying this into your own markdown file or copy it into a spreadsheet if you feel that is easier to work with.

| terminology | explanation |
| ----------- | ----------- |
|             |             |
|             |             |
|             |             |
|             |             |
|             |             |
|             |             |
|             |             |
|             |             |
