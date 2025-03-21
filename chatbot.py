from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

loader = PyPDFLoader('Anwar.pdf')

docs = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size = 100, chunk_overlap = 20)

split_docs = text_splitter.split_documents(docs)
# print(split_docs[0])

embedding = OllamaEmbeddings(model='gemma:2b')

vector = FAISS.from_documents(split_docs, embedding)

retriver = vector.as_retriever()
# print(retriver.invoke('What is your name?'))

prompt = ChatPromptTemplate([(
    """
You have to act like Rana. Your bio will be given in the context. People will ask question to you and 
answer the questions based on the provided context only. 
Please provide the most accurate response based on the question and answer in short.
<context>
{context}
<context>
Ouestion: {input}
Answer:
""")
])

llm = ChatGroq(model = 'deepseek-r1-distill-llama-70b')
# print(llm.invoke('What is the capital of bangladesh?'))

question = 'What is your name?'

document_chain = create_stuff_documents_chain(llm, prompt)

retrieval_chain = create_retrieval_chain(retriver, document_chain)

# llm_prompt = prompt.invoke({'context' : retriver.invoke(question), 'input' : question})

# print(llm.invoke(llm_prompt))

# print(retrieval_chain.invoke({'input' : question})['answer'])

# response = retrieval_chain.invoke({'input' : question})

st.header('Chat with Anwar')

input = st.text_input('Enter your query: ')

if st.button('Send'):
    response = retrieval_chain.invoke({'input' : input})
    st.write(response['answer'].split('</think>')[-1])

