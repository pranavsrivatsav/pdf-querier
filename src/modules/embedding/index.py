from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.embeddings import HuggingFaceEmbeddings
from utils import getConfig

gemini_apikey = getConfig("gemini_api_key")

def get_embedding_function(embedding_model):
    if (embedding_model == "gemini"):
        return GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=gemini_apikey)
    elif (embedding_model == "miniLM"):
        return HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    else:
        raise ValueError(f"Unknown model name: {embedding_model}")