# Exercise 4 - FastAPI

In this exercise, you get to work with fastapi to create APIs of different kinds. You'll get to know the simple patterns of CRUD in fastapi. Also you'll learn how to serve csv data, and serve machine learning models.

## 0. FastAPI glossary API

Read the data from this repository called `fastapi_glossary.json`. Create Pydantic model(s) of the data in a separate script called `data_processing.py`. 

a) Now create an endpoint `/glossary` which will return all words and their meaning. 

b) Create a query parameter to filter out a specific word 

c) Turn your API into a CRUD API, so that you can add glossary, update and delete glossary. 

d) Test out your API in Swagger UI. 

e) Test out your API using requests inside of a Jupyter notebook or a separate Python script. Try the different request types.

## 1. Serve MYH data 

Go into this page in [Myndigheten för yrkeshögskola (MYH)](https://www.myh.se/yrkeshogskolan/resultat-ansokningsomgangar/resultat-for-program) and download Resultat ansökningsomgång 2024. 

> [!NOTE]
> This dataset is in Swedish

We will in this exercise create an API to serve this dataset for downstream users. 

a) Start with doing EDA on this dataset in a Jupyter notebook. Especially on "Tabell 3". 

b) Make an API endpoint where you serve table 3 in JSON format for a read operation. 

c) Make endpoints where you could filter out a particular school.

d) Make endpoints where you could filter out a particular field. 

e) Make endpoint for approved (beviljad) and one for not approved (avslag).

f) Make an endpoint for some KPIs that you think is interesting for a particular stakeholder in mind. 

g) What else do you want to be able to serve? 



 






## 2. FastAPI mpg  

In this exercise 

a) 

## 2. Simulate a small company

a)

## 3. A grading assistant

a)

## 4. Theory questions

a) What is a REST API?

b) What is CRUD?

c) Why would you want to use an API, can't you just create everything in for example a streamlit app?

d) What does it mean with decoupling and tightly coupling?

e) What are some other frameworks to create APIs in Python?

f) How would you mix Python together with a JavaScript frontend?

g)

## Glossary

Fill in this table either by copying this into your own markdown file or copy it into a spreadsheet if you feel that is easier to work with.

| terminology     | explanation |
| --------------- | ----------- |
| uvicorn         |             |
| endpoint        |             |
| path parameter  |             |
| query parameter |             |
| routes          |             |
| request         |             |
| REST            |             |
| CRUD            |             |
| put             |             |
| post            |             |
| read            |             |
| update          |             |
| field_validator |             |
| Field           |             |
| response        |             |
| swagger ui      |             |
| OpenAPI         |             |
| curl            |             |
|                 |             |
|                 |             |
