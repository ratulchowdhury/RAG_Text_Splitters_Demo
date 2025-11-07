from langchain_experimental.text_splitter import SemanticChunker
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()



splitter = SemanticChunker(OpenAIEmbeddings())

sample_text = """
Machine learning models for retail price optimization analyze historical sales data and competitor pricing to maximize revenue while maintaining customer demand. Predictive algorithms can forecast optimal price points across thousands of SKUs, enabling dynamic pricing strategies that respond to market conditions in real time.

The James Webb Space Telescope captured infrared images of distant galaxies formed just 300 million years after the Big Bang, revealing unprecedented details about early cosmic structure. These observations challenge existing models of galaxy formation and suggest that massive galaxies assembled far more quickly than previously thought possible.

Credit card fraud detection systems leverage supervised learning on imbalanced datasets, using techniques like SMOTE and ensemble methods to identify fraudulent transactions with high precision. Feature engineering combines transaction velocity, geographic patterns, and spending anomalies to flag suspicious activity within milliseconds of card authorization.

Traditional Japanese tea ceremonies follow strict protocols refined over 400 years, emphasizing mindfulness, aesthetic appreciation, and social harmony through precise movements and carefully prepared matcha. The ceremony transforms a simple act of drinking tea into a meditative practice that embodies Zen Buddhist principles of simplicity and presence.
"""

print("Processing text with semantic chunking...")
docs = splitter.create_documents([sample_text])

print(f"\nTotal Chunks Created: {len(docs)}")
print("="*50)

# Display each chunk with its content
for i, doc in enumerate(docs, 1):
    print(f"\nChunk {i}:")
    print(f"Content: {doc.page_content.strip()}")
    print(f"Length: {len(doc.page_content)} characters")
    print("-" * 40)