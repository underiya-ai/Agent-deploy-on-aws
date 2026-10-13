from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_tavily import TavilySearch


load_dotenv()  # TAVILY_API_KEY aur GROQ_API_KEY .env se load hongi

# Tavily client (key apne aap env se le leta hai)
tavily = TavilySearch(
    max_results=3,
    search_depth="advanced",
)


llm = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite") # GROQ_API_KEY env se le leta hai


@tool
def search_tool(query: str) -> str:
    """Search the web for user queries or real-time data.

    Args:
        query: the user's search query
    """
    return tavily.invoke({"query": query})


agent = create_agent(
    model=llm,
    tools=[search_tool],
    system_prompt=(
        "You are a search agent. For user questions, call the 'search_tool' "
        "tool to get real-time details from the web."
    )
)