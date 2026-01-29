from pydantic_ai import Agent
from data_models import RagResponse
from constants import VECTOR_DB_PATH
import lancedb
from dotenv import load_dotenv

load_dotenv()


rag_agent = Agent(
    model="google-gla:gemini-2.5-flash",
    retries=2,
    system_prompt=(
        "You are an expert in rabbit races and knows how to distinguish between the rabbits",
        "Always answer based on the retrieved knowledge, but you can mix in your expertise to make the answer more coherent",
        "IMPORTANT: Don't hallucinate, rather say you can't answer it if the user prompts outside of the retrieved knowledge",
        "Make sure to keep the answer clear and concise, getting to the point directly, max 4 sentences",
        "Also describe which file you have used as source",
    ),
    output_type=RagResponse,
)

# create tool for rag_agent to use
@rag_agent.tool_plain
def retrieve_top_document(query: str, k=3) -> str:
    """
    uses vector search to find the closest k matching documents to query
    """

    # logic to connect to knowledge base
    vector_db = lancedb.connect(uri = VECTOR_DB_PATH)

    # retrieve most relevant document
    results = vector_db["articles"].search(query=query).limit(k).to_list()

    # pick out relevant info and construct a context for LLM to use
    return f"""

    Filename: {results[0]["doc_id"]}

    Filepath: {results[0]["filepath"]}

    Content: {results[0]["content"]}

    """