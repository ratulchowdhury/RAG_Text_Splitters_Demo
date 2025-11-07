from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("sample.pdf")
docs = loader.load()
splitter = CharacterTextSplitter(chunk_size = 200, chunk_overlap= 40, separator = "")
docs_split = splitter.split_documents(docs)
print(f"First Page Content",docs_split[0].page_content)
print(f"First Page Metadata",docs_split[0].metadata)