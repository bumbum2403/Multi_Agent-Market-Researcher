def industry_research_prompt(company_name, company_url):
    return f"""
    Research the industry that {company_name} operates in by visiting their website at {company_url}. Identify their key offerings, strategic focus areas, and provide a vision of the industry.
    """

def use_case_generation_prompt(industry_data):
    return f"""
    Based on the following industry data: {industry_data}, generate relevant AI use cases where the company can leverage Generative AI, LLMs, and ML technologies to enhance operational efficiency, improve customer satisfaction, and boost business processes.
    """

def resource_asset_collection_prompt(use_case_data):
    return f"""
    Based on the use cases: {use_case_data}, search for relevant datasets and research papers on platforms like Kaggle, HuggingFace, or GitHub. Save the resource links in a markdown file format.
    """
