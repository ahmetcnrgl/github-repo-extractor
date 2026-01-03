---
title: Github Repo Extractor
sdk: gradio
sdk_version: "5.9.1"
app_file: app.py
pinned: false
license: mit
---

# GitHub Repository Extractor

This application is an AI-powered tool designed to extract, analyze, and summarize repository information from GitHub profiles. It utilizes Large Language Models (LLMs) including GPT-4o, Claude 3.5 Sonnet, and Gemini 1.5 Flash to process unstructured HTML data into structured tables.

**Live Demo:** [Click here to view on Hugging Face Spaces](https://huggingface.co/spaces/ahmetcnrgl/github-repo-extractor)

## Features

* **Repository Scraping:** Fetches public repository data directly from GitHub profile tabs using Python requests and BeautifulSoup.
* **AI Analysis:** Leverages advanced LLMs to interpret repository context and programming languages.
* **Structured Output:** Generates a Markdown table containing the repository name, link, short English description, and primary language.
* **Model Selection:** Users can switch between OpenAI, Anthropic, and Google Gemini models via the interface.

## Tech Stack

* **Python 3.9+**
* **Gradio:** For the web interface.
* **BeautifulSoup4:** For parsing HTML content.
* **OpenAI / Anthropic / Google Generative AI:** For natural language processing.

## Installation

To run this project locally, follow the steps below:

1.  **Clone the repository**

    ```bash
    git clone [https://github.com/ahmetcnrgl/github-repo-extractor.git](https://github.com/ahmetcnrgl/github-repo-extractor.git)
    cd github-repo-extractor
    ```

2.  **Install requirements**

    ```bash
    pip install -r requirements.txt
    ```

3.  **Environment Configuration**

    Create a `.env` file in the root directory and add your API keys:

    ```env
    OPENAI_API_KEY=your_key_here
    ANTHROPIC_API_KEY=your_key_here
    GOOGLE_API_KEY=your_key_here
    ```

4.  **Run the Application**

    ```bash
    python app.py
    ```

## Usage

1.  Enter the full URL of a GitHub repositories tab (e.g., `https://github.com/username?tab=repositories`).
2.  Select the desired AI model from the dropdown menu.
3.  Click the submit button to generate the summary table.

## License

This project is licensed under the MIT License.
