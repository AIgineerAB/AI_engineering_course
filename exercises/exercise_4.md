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

## 2. Serve ML models

Read the [mpg dataset from kaggle](https://www.kaggle.com/datasets/uciml/autompg-dataset/code). In this exercise you'll need to develop a ML model to predict miles per gallon (mpg) for this dataset.

a) Do EDA on the dataset

b) Go through data science workflow and try out different models until you find one you want to choose.

c) Train on all data in the dataset with your chosen model

d) Now export the model with joblib

e) Read this model and create an API around it. You should have endpoints to be able to read the data, do some filterings and be able to send in data to get prediction back.

## 3. Consume your APIs

Instead of creating a frontend to directly (tightly coupled) with the data and backend, it's good to talk via an API layer. It's possible to change your frontend and keep the same backend if you do this and also frontend frameworks that is not in Python can't directly communicate with your backend if it's in Python. Use Streamlit or Taipy to consume each of your created APIs. Show some data, plot some graphs, make some interesting user interfaces for your end consumers.

Remember to also add descriptions on your frontend apps to explain what it does, limitations of models etc.

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
