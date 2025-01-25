from langchain_community.retrievers import TavilySearchAPIRetriever
from dotenv import load_dotenv
import os

# Load the environment variables from the .env file
load_dotenv()

# Fetch the Tavily API key from environment variables
api_key = os.getenv("TAVILY_API_KEY")
if not api_key:
    raise ValueError("TAVILY_API_KEY is not set in the environment variables.")

# Initialize TavilySearchAPIRetriever
tavily_search = TavilySearchAPIRetriever(api_key=api_key)

def search_industry_data(query):
    """Uses Tavily to search industry-specific data."""
    results = tavily_search.get_relevant_documents(query)
    return results
