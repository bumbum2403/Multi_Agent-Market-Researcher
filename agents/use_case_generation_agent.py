from langchain.agents import Agent
from langchain_community.llms import HuggingFaceHub
from dotenv import load_dotenv
import os
# Get Hugging Face API token
huggingface_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")
if not huggingface_token:
    raise ValueError("HUGGINGFACEHUB_API_TOKEN is not set in the environment variables.")


# Define the LLM model for Use Case Generation
llm = HuggingFaceHub(repo_id="bert-base-uncased", huggingfacehub_api_token=huggingface_token)

# Use Case Generation Agent
use_case_generation_agent = Agent(
    role="Use Case Generator",
    goal="Generate use cases for AI in the industry",
    backstory="You are an AI designed to generate use cases for AI in the industry.",
    verbose=True,
    allow_delegation=False,
    llm=llm
)
