import requests
from bs4 import BeautifulSoup

# List of blog URLs
blog_urls = [
    "https://www.leewayhertz.com/ai-use-cases-and-applications/#AI-use-cases-in-major-industries",
    "https://www.ibm.com/think/topics/artificial-intelligence-business-use-cases",
    "https://cloud.google.com/transform/101-real-world-generative-ai-use-cases-from-industry-leaders"
]

def scrape_blog(url):
    """Scrapes the content of the blog for training data."""
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    content = soup.get_text()
    return content

def scrape_all_blogs():
    """Scrapes all blogs and returns a combined text."""
    all_blog_data = ""
    for url in blog_urls:
        all_blog_data += scrape_blog(url)
    return all_blog_data
