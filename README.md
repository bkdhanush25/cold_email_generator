# Cold Email Generator

## Overview

The Cold Email Generator is an AI-powered tool that generates personalized cold email text for job applications. It uses the Groq Llama-3.3-70b-versatile model for generating professional emails based on a job description from a URL and a user's resume in PDF format. The system extracts relevant job information from the job page and writes an email based on the provided resume.

## Features

- Upload your resume (PDF format) and input a job description URL.
- Extracts job details like role, experience, skills, and description from the job page.
- Generates a customized cold email based on the extracted job information and the details from your resume.
- Built with the Groq Llama-3.3-70b-versatile model for text generation.

## Requirements

- Python 3.8 or later
- Libraries:
  - `langchain-community`
  - `langchain-groq`
  - `langchain-core`
  - `chromadb`
  - `uuid`
  - `python-dotenv`
  - `streamlit`
  - `pdfplumber`
  - `pysqlite3-binary`
- Groq API Key for using the Groq Llama model.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/bkdhanush25/cold_email_generator.git
    ```

2. Navigate into the project directory:

    ```bash
    cd cold_email_generator
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Create a `.env` file and add your Groq API key:

    ```
    GROQ_API_KEY=your_groq_api_key_here
    ```

## Usage

1. Run the Streamlit app:

    ```bash
    streamlit run app.py
    ```

2. In the app interface:
   - Upload your resume in PDF format.
   - Enter the URL of the job posting.
   - Click "Submit" to generate the cold email.

3. The system will process the job details from the URL and your resume, then generate a cold email tailored to the job description.

## Example

1. **Upload your resume** (PDF format).
2. **Enter a job URL**:

    ```
    https://example.com/job-opening
    ```

3. After clicking **Submit**, the app will display the generated cold email.

## Code Overview

### 1. **Resume Class** (`resume.py`)

The `Resume` class handles PDF resume parsing. It extracts the text from the resume using the `pdfplumber` library and stores it in a vector database (via `chromadb`) for easy retrieval.

### 2. **Chain Class** (`chains.py`)

The `Chain` class integrates with the Groq model for:
- Extracting job details from the scraped website using the `extract_jobs` method.
- Writing a cold email based on the extracted job description and the provided resume using the `write_mail` method.

### 3. **Text Cleaning** (`utils.py`)

The `clean_text` function processes raw text by:
- Removing HTML tags and URLs.
- Cleaning up special characters and multiple spaces.
- Standardizing the text for further processing.

## Contributing

Feel free to fork the repository, submit pull requests, and open issues. Contributions are always welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Groq Llama-3.3-70b-versatile model for generating the cold emails.

