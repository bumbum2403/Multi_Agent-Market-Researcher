
# Multi-Agent System for AI & GenAI Use Case Generation

This project is a **Multi-Agent System** designed to conduct market research, analyze industries, and generate relevant AI and GenAI use cases for specific companies or industries. The system is built with modularity and scalability in mind, enabling dynamic query handling and prompt-based responses.

---

## Features

1. **Industry Research Agent**:
   - Conducts market research using advanced web search tools (Tavily).
   - Analyzes industry trends, company information, and strategic focus areas.

2. **Use Case Generation Agent**:
   - Proposes AI/GenAI use cases tailored to the company’s needs, focusing on operational efficiency and customer satisfaction.

3. **Resource Asset Collection Agent**:
   - Collects datasets and resources from platforms like Kaggle, HuggingFace, and GitHub.
   - Outputs relevant resources for proposed AI solutions.

4. **Dynamic Query Handling**:
   - Supports dynamic queries such as:
     - "How is the retail industry leveraging AI and ML?"
     - "AI applications in automotive manufacturing."

5. **Gradio Interface**:
   - User-friendly interface for inputting company URLs or queries.
   - Outputs results in a chat-like format.

6. **Training LLM**:
   - LLM fine-tuned using domain-specific blog content for enhanced specialization.

---

## Project Structure

```
project/
│
├── agents/
│   ├── industry_research_agents.py
│   ├── use_case_generation_agent.py
│   ├── resource_asset_collection_agent.py
│   └── tavily_search.py
│
├── training/
│   ├── data/
│   │   ├── blog_data/
│   │   │   ├── leewayhertz_blog.json
│   │   │   ├── ibm_blog.json
│   │   │   └── google_cloud_blog.json
│   └── train_model.py
│
├── app/
│   └── gradio_interface.py
│
├── requirements.txt
├── main.py
└── README.md
```

---

## Prerequisites

- Python 3.13.1
- macOS (M1 chip or compatible)
- Hugging Face API Key
- Tavily API Key

---

## Installation

1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd project
   ```

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   - Create a `.env` file in the root directory:
     ```
     HUGGINGFACEHUB_API_TOKEN=your_huggingface_api_key
     TAVILY_API_KEY=your_tavily_api_key
     ```

---

## Usage

1. Train the LLM:
   ```bash
   python training/train_model.py
   ```

2. Run the application:
   ```bash
   python app/gradio_interface.py
   ```

3. Open the Gradio interface in your browser to interact with the system.

---

## Example Query

- Input: **"AI use cases in the retail industry"**
- Output: 
  - Suggested Use Cases: "Personalized product recommendations, supply chain optimization, automated inventory management."
  - Resource Links:
    - [Kaggle Dataset on Retail AI](https://www.kaggle.com)
    - [HuggingFace Model for NLP in Retail](https://huggingface.co)

---

## Contribution

Contributions are welcome! Feel free to submit issues or pull requests.

---

## License

This project is licensed under the MIT License.
