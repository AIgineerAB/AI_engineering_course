# Exercise 5 - PydanticAI and FastAPI

In this exercise, you get to work with fastapi to create APIs of different kinds. You'll get to know the simple patterns of CRUD in fastapi. Also you'll learn how to serve csv data, and serve machine learning models. You will also use pydanticai together with fastapi.

## 0. PydanticAI fundamentals

Make a PydanticAI model that can take an input of a location and then it should suggest 5 restaurants nearby that place. The restaurant model should have

- name
- type of food (cuisine)
- price level
- rating
- short description
- opening hours
- location

It's okay if your model is making up a restaurant that doesn't exist

## 1. FastAPI to serve PydanticAI

Now make a fastapi with a post endpoint in natural language to prompt for a location and what type of food. Based on these it should generate a restaurant and store it in a duckdb database.

Also implement a get endpoint for showing all restaurants in the database. Implement a simple frontend for this application.

## 2. Extend Books API

Add a post endpoint to 08_fast_api_crud that can take a natural language prompt, which will create a new book.


## 3. Frontend for movies example

Create a frontend for movies example in 11b.

## Theory questions

a) What problem does PydanticAI solve when using LLMs?

b) Why is schema validation critical in LLM-based systems?

c) What risks exist if retries are unlimited?

d) How can FastAPI be used to serve PydanticAI? Give an example

e) Why is PydanticAI’s validated output better than plain-text LLM responses?

## Glossary

Fill in this table either by copying this into your own markdown file or copy it into a spreadsheet if you feel that is easier to work with.

| terminology          | explanation |
| -------------------- | ----------- |
| tools                |             |
| dependencies         |             |
| output_type          |             |
| dependency injection |             |
| request body         |             |
| response model       |             |
| pydantic model       |             |
| Agent                |             |
| output_type          |             |
| model                |             |
| run                  |             |
| system prompt        |             |
| retry loop           |             |
| tool call            |             |
| messages             |             |
|                      |             |
