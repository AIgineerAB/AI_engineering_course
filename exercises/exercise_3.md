# Exercise 3 - pydantic

In this exercise, you get to work with data validation using Pydantic v2 and Gemini. Output in general from LLMs are unstructured and hard to work with, to get any value from it you need to structure the output and validate its contents. This can be done with Pydantic.

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

## 3. A grading assistant

Teachers in general have a lot of administrations to do and one of those things is grading. Can we create a simple grade assistant to assist a Swedish teacher in grading? This exercise focuses a lot in prompt engineering and afterwards to postprocess the output using Pydantic.

a) [Go into this page with examples of students answers](https://www.uu.se/download/18.11971c6f1989761a6625867/1755009079925/Svsva%20Niv%C3%A5%201%20Del%20C%20Resonerande%20uppgift,%20matris,%20analys.pdf) to a particular question. Copy some example texts and paste it into files with names like `student_text_1.txt`, `student_text_2.txt`.

b) Read these data into python and tell your LLM to grade them.

c) Prompt to get an output of fields proposed_grade, motivation and improvements.

d) Now validate this with pydantic model

e) Output a folder with the following txt files: proposed_grade.txt, motivation.txt and improvements.txt

f) Go [into skolverket for Svenska 1](https://www.skolverket.se/undervisning/gymnasieskolan/program-och-amnen-i-gymnasieskolan/hitta-program-amnen-och-kurser-i-gymnasieskolan-gy11/amne?url=907561864%2Fsyllabuscw%2Fjsp%2Fsubject.htm%3FsubjectCode%3DSVE%26version%3D8%26tos%3Dgy&sv.url=12.5dfee44715d35a5cdfa92a3) and copy "Betygskriterier" for "Svenska 1". These are the criterias for the different grades. Paste this into a file called `criterias.txt`.

g) Now repeat b)-e) but with the criterias in your prompt as well. Can you see any differences in the outputs?

h) Can you improve the output quality by providing few shot examples?

## 4. Theory questions

a) Explain the primary purpose of Pydantic. What core problems does it solve for developers?

b) In Pydantic, what is the key difference between using model_validate() and model_validate_json()? When would you use each one?

c) How can you define a field in a Pydantic model that has a specific value constraint, such as a minimum or maximum number? Give an example.

d) Describe how Pydantic's data validation can improve the robustness and reliability of an application that processes data from an external API.

e) What is a computed field in Pydantic?

f) What are tokens in LLMs?

g) Large language models (LLMs) can struggle to generate a large amount of structured data, like 100 JSON objects in a single request, primarily due to token limitations and context window constraints.

h) What are some strategies you can use to make an LLM's output more reliable when you need it to produce a specific format, such as JSON or Markdown?

i) What are few shot examples?

## Glossary

Fill in this table either by copying this into your own markdown file or copy it into a spreadsheet if you feel that is easier to work with.

| terminology        | explanation |
| ------------------ | ----------- |
| few shot learning  |             |
| token              |             |
| context window     |             |
| pydantic           |             |
| BaseModel          |             |
| Field              |             |
| model_fields       |             |
| computed_field     |             |
| model_validate     |             |
| model_dump         |             |
| type hinting       |             |
| serialization      |             |
| deserialization    |             |
| prompt engineering |             |
| zero-shot learning |             |
