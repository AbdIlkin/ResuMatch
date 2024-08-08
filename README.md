# ResuMatch

ResuMatch is a Streamlit application that helps users review their resumes using AI. By uploading a PDF resume and providing a job description, the app leverages large language models (LLMs) to evaluate the resume against the job requirements and provide actionable insights.

## Features

- **Resume Evaluation**: Get a professional evaluation of your resume against a specific job description.
- **Skill Improvement Suggestions**: Receive advice on enhancing your skills based on your resume and the job description.
- **Keyword Analysis**: Identify missing keywords that are critical for Applicant Tracking Systems (ATS).
- **Percentage Match**: Determine how well your resume matches the job description, including missing keywords and final thoughts.

## Project Structure

- `app.py`: Main Streamlit application file.
- `pdf_processing.py`: Handles PDF text extraction.
- `ai_responses.py`: Manages AI model interaction and response caching.
- `prompts.py`: Contains prompt templates used for AI interactions.
- `responses.json`: Stores cached responses for faster processing.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/your-repository-name.git
    cd your-repository-name
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up your environment variables:

    - Create a `.env` file in the root directory and add your Google API key:
    
    ```env
    GOOGLE_API_KEY=your_google_api_key_here
    ```

4. Run the application:

    ```bash
    streamlit run app.py
    ```

## Usage

- Upload a PDF of your resume.
- Paste the job description in the provided text area.
- Choose an option to evaluate your resume, improve your skills, identify missing keywords, or calculate the percentage match.
- View the AI-generated insights and recommendations.



"# ResuMatch" 
"# ResuMatch" 
"# ResuMatch" 
