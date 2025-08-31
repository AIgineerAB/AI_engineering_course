# Exercise 3 - pydantic

In this exercise, you get to work with data validation using pydantic v2

## NOT DONE YET

## 0. Pydantic warmup

This exercise will give you a feel of the pydantic library for data validation. 

a) Create a BaseModel for a User. It should have a required id (integer) and a required name (string). Instantiate the model with valid data and then with invalid data (e.g., a string for id) to see the ValidationError.

b) Create a BaseModel for a Person with the fields name, age, email, favourite pet. Add appropriate validation in each fields. Tips: you can use built-in EmailStr type in pydantic for validating email. Try out your Person class by instantiating it with different types of values for the fields to see proper validations. 

c) Use normal python class to replicate what you have created in b), i.e. create a Person class with proper input validation. 

## 1. Validate data from API using Pydantic

Use this code snippet to get a random dad joke 

```py
import requests

headers = {"Accept": "application/json"}
response = requests.get("https://icanhazdadjoke.com/", headers=headers)

print(response.json())
```

a) Create a Pydantic model with name Joke with the following fields 

- id with type integer  
- joke with type string

b) Validate the data from the API using the Joke model. Test out your Joke instance to see that you can access the joke and id fields. 

c) Now create a new Joke Pydantic model that also have the field words_in_joke. This is a computed field and a property so you will need to decorate your method like this 

```py   
    @computed_field
    @property
    def words_in_joke(self) -> int:
        """returns number of words in the joke"""
```

Note that computed_field is imported from pydantic. Validate a random joke with your new Joke model.

d) Request 10 jokes from the api and validate them into many Jokes instances that you store into a list. Make sure to use sleep for 5 seconds to not request from the API too much. 



## 2. Simulate a small company 

a) Connect python to gemini, very important that you place the api key in .env and gitignore it 

b) Use gemini to simulate 20 data points in json format containing the following fields: first_name, last_name, phone_number, email, department, salary, title. See if you can prompt to direct the LLM output to have swedish names, phone numbers in swedish format (+46 731 29 52), departments (IT, HR, marketing, sales), reasonable salary (you might need to check some swedish statistics on salaries) and corresponding titles within these departments. 

c) Now use pydantic to validate this json and put in proper schema that the fields should follow. You might need to do some processing such as removing backticks and maybe loading json data into a list with `json.loads()`. Also make sure that only correctly validated data should be stored. 

d) Write this json data to a folder called output_data. 

e) Use pandas to read the data as dataframe

f) Write a csv file to your output_data

g) Load this data into a staging layer and store this into a table called employees. 

h) Use gemini to simulate departments data. There should be same departments as those you had in task b. Also add a description field and a contact person. 

i) Add a departments table in your duckdb database under staging layer to store this data. 


## 3. 

a)

b)

c)

d)

e)

f)

## 4. Theory questions

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
