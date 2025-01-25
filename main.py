import gradio as gr
from agents.industry_research_agents import industry_research_agent
from agents.use_case_generation_agent import use_case_generation_agent
from agents.resource_asset_collection_agent import resource_asset_collection_agent
from utils.blog_scraper import scrape_all_blogs
from utils.prompt_templates import industry_research_prompt, use_case_generation_prompt, resource_asset_collection_prompt
from utils.tavily_search import search_industry_data
from utils.train_model import train_model_on_blog_data
from langchain_community.llms import HuggingFaceHub

def run_agent_workflow(company_name, company_url):
    # Step 1: Scrape blogs to get training data
    blog_data = scrape_all_blogs()
    
    # Step 2: Train the model on the scraped blog data
    train_model_on_blog_data(blog_data)
    
    # Step 3: Run industry research agent
    industry_prompt = industry_research_prompt(company_name, company_url)
    industry_data = industry_research_agent.run(industry_prompt)
    
    # Step 4: Run use case generation agent
    use_case_prompt = use_case_generation_prompt(industry_data)
    use_case_data = use_case_generation_agent.run(use_case_prompt)
    
    # Step 5: Run resource asset collection agent
    resource_prompt = resource_asset_collection_prompt(use_case_data)
    resource_links = resource_asset_collection_agent.run(resource_prompt)
    
    # Step 6: Search industry data using Tavily (Optional)
    tavily_results = search_industry_data(f"{company_name} AI applications")
    
    # Return the results
    return industry_data, use_case_data, resource_links, tavily_results

# Define Gradio interface
def gradio_interface(company_name, company_url):
    results = run_agent_workflow(company_name, company_url)
    return f"Industry Data: {results[0]}\nUse Cases: {results[1]}\nResource Links: {results[2]}\nTavily Search Results: {results[3]}"

# Gradio UI
interface = gr.Interface(fn=gradio_interface, 
                         inputs=["text", "text"], 
                         outputs="text", 
                         live=True)

# Launch Gradio app
if __name__ == "__main__":
    interface.launch()
