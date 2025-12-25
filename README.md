#  GitHub Repo Extractor with OpenAI

This project is an intelligent tool that scrapes public repositories from a GitHub profile and formats them into a clean, organized Markdown list using **OpenAI's GPT-4o-mini**.

It demonstrates the extraction of unstructured data (HTML) and its conversion into structured outputs using Large Language Models (LLMs).

##  Features

- **Web Scraping:** Extracts raw links from GitHub profile pages using `BeautifulSoup` and `Requests`.
- **LLM Integration:** Uses OpenAI API to intelligently filter and format repository data.
- **Smart Formatting:** Converts raw data into a clean, clickable Markdown list suitable for portfolios or brochures.
- **Modular Design:** Separates scraping logic (`scraper.py`) from the analysis workflow (`main.ipynb`).

##  Tech Stack

- **Python 3.x**
- **OpenAI API** (GPT-4o-mini)
- **BeautifulSoup4** (Web Scraping)
- **Jupyter Notebook** (Interactive Development)

##  Project Structure


github-repo-extractor/
├── main.ipynb          # Main notebook with LLM logic and workflow
├── scraper.py          # Helper script for web scraping
├── requirements.txt    # Project dependencies
├── .env.example        # Template for environment variables
├── .gitignore          # Files to ignore (e.g., .env, venv)
└── README.md           # Project documentation



##  Installation & Setup

1. **Clone the repository:**

git clone [https://github.com/ahmetcnrgl/github-repo-extractor.git](https://github.com/ahmetcnrgl/github-repo-extractor.git)
cd github-repo-extractor



2. **Create a virtual environment (Optional but recommended):**

python -m venv .venv
# Windows:
.venv\Scripts\activate
# Mac/Linux:
source .venv/bin/activate



3. **Install dependencies:**

pip install -r requirements.txt



4. **Set up API Key:**
* Rename `.env.example` to `.env`.
* Add your OpenAI API Key inside the file:

OPENAI_API_KEY=sk-proj-your-actual-api-key-here






##  Usage

1. Open `main.ipynb` in Jupyter Notebook or VS Code.
2. Run the cells sequentially to initialize the environment and functions.
3. Call the main function with a GitHub username and repository tab URL:


create_link_selector("ahmetcnrgl", "[https://github.com/ahmetcnrgl?tab=repositories](https://github.com/ahmetcnrgl?tab=repositories)")


### Example Output

The tool will generate a Markdown output like this:
<img width="1275" height="418" alt="image" src="https://github.com/user-attachments/assets/d0d09679-4308-4a7c-9e87-fd271f18fac6" />



##  Note

This project is for educational purposes. Please ensure you have your own OpenAI API key to run the LLM components.

---

*Developed by ahmetcnrgl

```

```
