from fastapi import FastAPI
from backend.rag import rag_agent
from backend.data_models import Prompt

app = FastAPI()

@app.get("/test")
async def test():
    return {"test": "hello"}


@app.post("/rag/query")
async def query_documentation(query: Prompt):
    result = await rag_agent.run(query.prompt)
    
    return result.output