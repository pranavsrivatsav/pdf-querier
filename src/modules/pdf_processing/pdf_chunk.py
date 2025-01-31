from langchain.text_splitter import RecursiveCharacterTextSplitter

def chunk_pdf(input, inputType = "documents"):
    # Split the text into chunks
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1500,
        chunk_overlap=200,
        length_function=len,
        separators=["\n\n", "\n", " "]
    )

    chunks = None

    if inputType == "documents":
        chunks = text_splitter.split_documents(input)
    elif inputType == "text":
        chunks = text_splitter.split_text(input)
    else:
        raise ValueError("Invalid inputType")
    print(f"Number of chunks: {len(chunks)}")
    return chunks