# Exercise 6 - Creating chatbots

In this exercise, you get to work with pydanticai to create different types of chatbots.

## 0. Different themes

Create a chatbot similar to lecture [12_pydanticai_chatbot](https://github.com/AIgineerAB/AI_engineering_course/tree/main/12_pydanticai_chatbot) but with different themes. In the frontend it should be possible to change which theme you want the chatbot to become.

a) A storyteller that tells stories to children

b) An instructor that is good at helping students to improve in programming

c) A sports commentator that always answers with a cool sports comment.

d) A joker, that always answers with a nerdy joke

e) something else of your choice

## 1. LanceDB

In order to make a chatbot have long-term memory we will need to have documents stored in a vector database which can do matching between queries and prompts. One such vector database is lancedb. Here we'll work with lancedb to learn the tool.

Note that these articles are from wikipedia

a) There are 6 articles in [data](https://github.com/AIgineerAB/AI_engineering_course/tree/main/exercises/data). Download these and ingest them into lancedb. Embed these articles as well using gemini embedding.

b) Now type in a few questions and embed these, then do vector search to find the most relevant articles

## 2. RAG

Based on the articles and the lancedb database in the previous exercise, create a RAG application so that you can chat with your documentation. Now also create a fastapi to serve this RAG and a streamlit frontend to consume it.

## Theory questions

a) What is the purpose of doing a RAG compared to normal chatbot?

b) An agent can have three types of memory: short-term, long-term and internal. If the agent has a RAG as a tool, which of these would it correspond to?

c) What happens when using different embedding models for embedding the query and the knowledge database?

d) What are zero-shot learning and few shot learning?

e) Isn't it enough with advanced prompt engineering, why do we need RAG?

## Glossary

Fill in this table either by copying this into your own markdown file or copy it into a spreadsheet if you feel that is easier to work with.

| terminology       | explanation |
| ----------------- | ----------- |
| RAG               |             |
| embedding         |             |
| vector database   |             |
| ANN               |             |
| KNN               |             |
| retriever         |             |
| generator         |             |
| similarity search |             |
| BM25              |             |
| keyword search    |             |
| hybrid search     |             |
| vector search     |             |
| cosine similarity |             |
| chunking          |             |
| context           |             |
| context window    |             |
| metadata          |             |
| agentic rag       |             |
