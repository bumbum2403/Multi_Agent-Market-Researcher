from langchain.agents import Agent
from langchain_community.llms import HuggingFaceHub
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Get Hugging Face API token
huggingface_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")
if not huggingface_token:
    raise ValueError("HUGGINGFACEHUB_API_TOKEN is not set in the environment variables.")

# Initialize HuggingFaceHub
llm = HuggingFaceHub(repo_id="bert-base-uncased", huggingfacehub_api_token=huggingface_token)
# Define the LLM model for Industry Research
llm = HuggingFaceHub(repo_id="bert-base-uncased")



# Industry Research Agent
industry_research_agent = Agent(
    role="Industry Researcher",
    goal="Research industry trends and key players",
    backstory="You are an AI designed to research industry trends and key players.",
    verbose=True,
    allow_delegation=False,
    llm=llm
)
