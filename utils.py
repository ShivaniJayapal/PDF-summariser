
#from langchain.document_loaders import PyPDFLoader
from langchain_community.document_loaders import PyPDFLoader

from langchain.text_splitter import CharacterTextSplitter
from langchain.chat_models import ChatOpenAI
from langchain.chains.summarize import load_summarize_chain

def load_pdf_text(pdf_path):
    loader = PyPDFLoader(pdf_path)
    pages = loader.load()
    return pages

def summarize_pdf(pages, openai_api_key):
    text_splitter = CharacterTextSplitter(separator="\n", chunk_size=1000, chunk_overlap=200)
    docs = text_splitter.split_documents(pages)

    llm = ChatOpenAI(temperature=0, openai_api_key=openai_api_key)
    chain = load_summarize_chain(llm, chain_type="map_reduce")

    summary = chain.run(docs)
    return summary
