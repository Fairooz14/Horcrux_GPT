# Horcrux GPT 🪄
#### A Student Assistant ChatGPT

This project is a Streamlit-based application that allows users to upload multiple PDF files and ask questions about their content. It also provides general AI responses for questions outside the context of the uploaded PDFs using Google's Generative AI.

## Features

- Upload multiple PDF files.
- Extract text from the uploaded PDFs.
- Break down the text into manageable chunks.
- Store text chunks in a vector database using FAISS and Google Generative AI embeddings.
- Ask questions about the content of the PDFs.
- Provide general AI responses for questions outside the context of the PDFs.
- Stream responses in real-time.

## Getting Started

### Prerequisites

- Python 3.7 or higher
- A Gemini AI API key

### Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
2. Create a virtual environment and activate it:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
3. Install the required packages:
   ```sh
   streamlit==1.14.0
   python-dotenv==0.21.0
   PyPDF2==2.10.0
   langchain==0.0.113
   faiss-cpu==1.7.2
   google-generative-ai==0.0.1
4. Add your own Google API key to the  `.env` file:
   ```sh
   GOOGLE_API_KEY=your-google-api-key #from gemini studio

### Running the Application

1. Run the Streamlit application:
   ```sh
   streamlit run app.py

### Project Structure

- `assist.py`: The main application file that contains the Streamlit app logic.
- `htmlTemplates.py`: Contains HTML templates for the Streamlit app.
- `.env`: File to store environment variables ( such as API Key ).
- `raw_features`: Folder where you can find files to understand the pdf features and general text separately.

### Usage
1. Responses general chat  and answer any question before uploading any PDF.
2. Now upload one or more PDF files using the sidebar.
3. Click the "Process" button to extract and process the text from the PDFs.
4. Ask a question in the text input box. If the question is related to the PDF content, the application will provide an answer based on the PDF context.

## Technologies Used

- [Streamlit](https://streamlit.io/): Web framework for creating interactive web applications.
- [PyPDF2](https://pypdf2.readthedocs.io/): Library for reading PDF files.
- [LangChain](https://www.langchain.com/): Framework for building applications with large language models.
- [FAISS](https://github.com/facebookresearch/faiss): Library for efficient similarity search and clustering of dense vectors.
- [Google Generative AI](https://ai.google.dev/gemini-api): API for generative AI models.
