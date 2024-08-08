import google.generativeai as genai
import os
import hashlib
import json

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Define JSON file path
JSON_FILE_PATH = 'responses.json'

# Load existing responses from JSON file
def load_responses():
    if os.path.exists(JSON_FILE_PATH):
        with open(JSON_FILE_PATH, 'r') as file:
            return json.load(file)
    return {}

# Save responses to JSON file
def save_responses(data):
    with open(JSON_FILE_PATH, 'w') as file:
        json.dump(data, file, indent=4)

# Initialize response cache
response_cache = load_responses()

def get_gemini_response(prompt, resume_text, job_description):
    # Create a unique key based on resume text and job description
    base_key = hashlib.sha256((resume_text + job_description).encode()).hexdigest()
    prompt_key = hashlib.sha256(prompt.encode()).hexdigest()
    
    if base_key not in response_cache:
        response_cache[base_key] = {}
    
    if prompt_key in response_cache[base_key]:
        return response_cache[base_key][prompt_key]
    
    input_text = prompt.format(text=resume_text, jd=job_description)
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(input_text)
    
    # Cache and save the response
    response_text = response.text
    response_cache[base_key][prompt_key] = response_text
    save_responses(response_cache)
    return response_text
