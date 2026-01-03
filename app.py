import os
from dotenv import load_dotenv
from openai import OpenAI
import gradio as gr
from scraper import fetch_website_contents

load_dotenv(override=True)
openai_api_key = os.getenv('OPENAI_API_KEY')
anthropic_api_key = os.getenv('ANTHROPIC_API_KEY')
google_api_key = os.getenv('GOOGLE_API_KEY')

if openai_api_key:
    print(f"OpenAI API Key exists and begins {openai_api_key[:8]}")
else:
    print("OpenAI API Key not set")
    
if anthropic_api_key:
    print(f"Anthropic API Key exists and begins {anthropic_api_key[:7]}")
else:
    print("Anthropic API Key not set")

if google_api_key:
    print(f"Google API Key exists and begins {google_api_key[:8]}")
else:
    print("Google API Key not set")


openai = OpenAI()

anthropic_url = "https://api.anthropic.com/v1/"
gemini_url = "https://generativelanguage.googleapis.com/v1beta/openai/"

anthropic = OpenAI(api_key=anthropic_api_key, base_url=anthropic_url)
gemini = OpenAI(api_key=google_api_key, base_url=gemini_url)



system_message = """You are an expert GitHub profile analysis assistant.

Your task is to analyze the scraped website text provided to you and find and list the GitHub repositories within it.

Rules:
1. Only identify projects/repositories. Skip menus and unnecessary text.
2. ALWAYS provide the output as a Markdown Table.
3. The table should have the following columns:
- **Repository Name**: The name of the project.
- **Link**: The link to the project.
- **Short Description**: Summarize what the project is about in one sentence in English.
- **Language**: The main programming language used.

If you find no repositories, write "No repositories found"."""


def stream_model(url, model):
    website_content = fetch_website_contents(url)
    
    prompt = f"Please analyze this repo link \n {website_content}"
    
    messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": prompt}
    ]

    if model == "GPT":
        stream = openai.chat.completions.create(
            model='gpt-4o-mini',
            messages=messages,
            stream=True
        )
    elif model == "Claude":
        stream = anthropic.chat.completions.create(
            model='claude-3-5-sonnet-20240620',
            messages=messages,
            stream=True
        )
    elif model == "Gemini":
        stream = gemini.chat.completions.create(
            model='gemini-2.5-flash', 
            messages=messages,
            stream=True
        )
    else:
        raise ValueError("Unknown model")

    result = ""
    for chunk in stream:
        result += chunk.choices[0].delta.content or ""
        yield result



message_in=gr.Textbox(label="Enter a github repositories URL",info="Example: https://github.com/JonasNilson?tab=repositories")
message_out=gr.Markdown(label="Output")
select_model=gr.Dropdown(["GPT","Claude","Gemini"],label="Select a model",value="GPT")

view = gr.Interface(
    fn=stream_model,
    title="Github Repo Extractor",
    inputs=[message_in,select_model],
    outputs=message_out,
    flagging_mode="never",
    examples=[
        ["https://github.com/JonasNilson?tab=repositories"],
        ["https://github.com/ahmetcnrgl?tab=repositories"],
    ])

view.launch(share=True)

