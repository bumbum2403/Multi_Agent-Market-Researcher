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

# Resource Asset Collection Agent
resource_asset_collection_agent = Agent(
    role="Resource Asset Collector",
    goal="Collect relevant datasets and resources for proposed AI use cases.",
    backstory="You are an AI designed to gather resource assets such as datasets and research papers.",
    verbose=True,
    allow_delegation=False,
    llm=llm
)
