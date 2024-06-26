import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import google.generativeai as genai
from langchain.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from htmlTemplates import css, bot_template, user_template

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

    
#Extracting Text from uploaded PDF.

def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

# Breaking down the texts into several Chuncks
def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=10000,
        chunk_overlap=1000
    )
    chunks = text_splitter.split_text(text)
    return chunks

# Chucks are stored in a vector database in embedded formet using Gemini
def get_vector_store(text_chunks):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vector_store = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    return vector_store

def get_conversation_chain():
    prompt_template = """
        Answer the question clear and precise. If not provided the context return the result as
        "Sorry I dont know the answer", don't provide the wrong answer.
        Context:\n {context}?\n
        Question:\n{question}\n
        Answer:
    """
    model = ChatGoogleGenerativeAI(model="gemini-pro", temperature=1.0)
    prompt = PromptTemplate(template=prompt_template, input_variables=['context', 'question'])
    chain = load_qa_chain(model, chain_type='stuff', prompt=prompt)
    return chain

def user_input(user_question, vector_store):
    embeddings = GoogleGenerativeAIEmbeddings(model='models/embedding-001')
    docs = vector_store.similarity_search(user_question)

    chain = get_conversation_chain()
    response = chain(
        {"input_documents": docs, "question": user_question},
        return_only_outputs=True
    )
    st.write(user_template.replace("{{MSG}}", response["output_text"]), unsafe_allow_html=True)
    

def main():
    st.set_page_config(page_title="Chat with multiple PDFs",
                       page_icon=":magic_wand:")
    st.write(css, unsafe_allow_html=True)
    #st.write(bot_template, unsafe_allow_html=True)

    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None

    st.header("ChatGPT :magic_wand:")
    user_question = st.text_input("Ask a Question from the PDF Files")
    
    #profile_pic_base64 = get_base64_image('images/profile_pic.png')
    

    if user_question and st.session_state.vector_store:
        user_input(user_question, st.session_state.vector_store)

    with st.sidebar:
        pdf_docs = st.file_uploader(
            "Upload your PDF Files and Click on Process", 
            accept_multiple_files=True
        )
        if st.button("Process"):
            with st.spinner("Processing..."):
                raw_text = get_pdf_text(pdf_docs)
                text_chunks = get_text_chunks(raw_text)
                st.session_state.vector_store = get_vector_store(text_chunks)
                st.session_state.conversation = get_conversation_chain()
                st.success("Done")

if __name__ == "__main__":
    main()
