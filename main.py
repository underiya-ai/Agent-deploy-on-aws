from src.agent_with_aws.agent import agent as search_agent
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Search Agent End Point")


class Search(BaseModel):
    query: str
    


@app.post("/agent_search")
def agent_search_endpoint(request: Search) -> dict:
    query = request.query

    result = search_agent.invoke({
        "messages": [
            {"role": "user", "content": query}
        ]
    })

    answer = result["messages"][-1].content

    return {
        "question": query,
        "Answer": answer
    }