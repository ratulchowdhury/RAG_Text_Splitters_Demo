from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("sample.pdf")
docs = loader.load()
splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=40)
chunks = splitter.split_documents(docs)
print(f"First Page Content: {chunks[0].page_content}") 
print(f"First Page Metadata: {chunks[0].metadata}")