from langchain.document_loaders import PyPDFLoader
from pdf_chunk import chunk_pdf
from pdf_image_processing import parse_pdf_image_and_chunk

def parse_pdf_and_chunk(pdf_path):
    # Load the PDF
    loader = PyPDFLoader(pdf_path)
    pages = loader.load()
    
    chunks = chunk_pdf(pages)
    chunk_type = "documents"

    if(len(chunks) == 0):
        chunks = parse_pdf_image_and_chunk(pdf_path)
        chunk_type = "text"
        
    return {"chunks": chunks, "chunk_type": chunk_type}