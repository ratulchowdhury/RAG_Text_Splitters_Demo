# RAG Text Splitters Demo

A comprehensive demonstration of different text splitting techniques for Retrieval-Augmented Generation (RAG) applications using LangChain.

## Overview

This repository showcases various text splitting strategies that are essential for building effective RAG systems. Text splitting is crucial for breaking down large documents into manageable chunks that can be effectively embedded and retrieved.

## Features

### 📚 Text Splitter Types Demonstrated

1. **Length-Based Text Splitter** (`length_based_text_splitter_demo.py`)
   - Uses `CharacterTextSplitter` for simple character-based splitting
   - Fixed chunk sizes with configurable overlap
   - Best for uniform text with consistent structure

2. **Structure-Based Text Splitter** (`text_structure_based_splitter_demo.py`)
   - Uses `RecursiveCharacterTextSplitter` for intelligent splitting
   - Respects document structure and natural boundaries
   - Ideal for maintaining context and readability

3. **Semantic Text Splitter** (`semantic_text_splitter_demo.py`)
   - Uses `SemanticChunker` with OpenAI embeddings
   - Splits text based on semantic similarity
   - Perfect for preserving topical coherence

## Prerequisites

### Environment Setup

1. **Python Requirements**: Python 3.8+
2. **API Keys**: OpenAI API key for semantic splitting
3. **Dependencies**: See `requirements.txt`

### Installation

```bash
# Clone the repository
git clone https://github.com/ratulchowdhury/RAG_Text_Splitters_Demo.git
cd RAG_Text_Splitters_Demo

# Create virtual environment
python -m venv .venv
.venv\Scripts\activate  # Windows
# source .venv/bin/activate  # Linux/Mac

# Install dependencies
pip install -r requirements.txt
```

### Environment Configuration

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your-openai-api-key-here
HUGGINGFACE_API_KEY_FINEGRAINED=your-huggingface-token-here  # Optional
```

## Usage

### Running the Demos

1. **Length-Based Text Splitter**:
   ```bash
   python length_based_text_splitter_demo.py
   ```

2. **Structure-Based Text Splitter**:
   ```bash
   python text_structure_based_splitter_demo.py
   ```

3. **Semantic Text Splitter**:
   ```bash
   python semantic_text_splitter_demo.py
   ```

### Sample Output

Each demo processes sample text and displays:
- Number of chunks created
- Content of each chunk
- Chunk sizes and characteristics
- Splitting methodology used

## Text Splitter Comparison

| Splitter Type | Best Use Case | Pros | Cons |
|---------------|---------------|------|------|
| **Character-Based** | Uniform text, simple documents | Fast, predictable sizes | May break sentences/context |
| **Recursive** | Structured documents, code | Respects boundaries, flexible | More complex setup |
| **Semantic** | Topic-based content, articles | Preserves meaning, coherent chunks | Requires API calls, slower |

## Configuration Options

### Length-Based Splitter
```python
CharacterTextSplitter(
    chunk_size=200,        # Characters per chunk
    chunk_overlap=40,      # Overlap between chunks
    separator="\n"         # Split separator
)
```

### Structure-Based Splitter
```python
RecursiveCharacterTextSplitter(
    chunk_size=200,        # Target chunk size
    chunk_overlap=40,      # Overlap for context
    separators=["\n\n", "\n", " ", ""]  # Priority order
)
```

### Semantic Splitter
```python
SemanticChunker(
    OpenAIEmbeddings(),    # Embedding model
    breakpoint_threshold_type="percentile",  # Threshold type
    breakpoint_threshold_amount=95          # Sensitivity
)
```

## Dependencies

Core dependencies include:
- `langchain` - Main framework
- `langchain-text-splitters` - Text splitting utilities
- `langchain-experimental` - Semantic chunker
- `langchain-openai` - OpenAI integration
- `langchain-community` - Community extensions
- `pypdf` - PDF processing
- `python-dotenv` - Environment variable management

See `requirements.txt` for complete dependency list.

## Project Structure

```
RAG_Text_Splitter/
├── length_based_text_splitter_demo.py    # Character-based splitting
├── text_structure_based_splitter_demo.py # Recursive splitting
├── semantic_text_splitter_demo.py        # Semantic splitting
├── requirements.txt                       # Python dependencies
├── .env                                   # Environment variables
├── .gitignore                            # Git ignore rules
├── sample.pdf                            # Sample document
└── README.md                             # This file
```

## Troubleshooting

### Common Issues

1. **Import Errors**: 
   - Ensure virtual environment is activated
   - Check that all packages are installed: `pip install -r requirements.txt`

2. **API Key Errors**:
   - Verify `.env` file contains valid OpenAI API key
   - Check API key permissions and usage limits

3. **Version Compatibility**:
   - Use compatible versions: `langchain-openai==0.2.9`
   - Avoid mixing different major versions of LangChain packages

### Version Notes

- **LangChain Migration**: Updated from deprecated `langchain.text_splitter` to `langchain_text_splitters`
- **Compatibility**: Uses `langchain-openai==0.2.9` for stability with `langchain-core==0.3.x`

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is open source and available under the [MIT License](LICENSE).

## References

- [LangChain Documentation](https://python.langchain.com/)
- [Text Splitters Guide](https://python.langchain.com/docs/concepts/#text-splitters)
- [RAG Best Practices](https://python.langchain.com/docs/tutorials/rag/)

## Author

**Ratul Chowdhury**
- GitHub: [@ratulchowdhury](https://github.com/ratulchowdhury)
- Repository: [RAG_Text_Splitters_Demo](https://github.com/ratulchowdhury/RAG_Text_Splitters_Demo)

---

*Last Updated: November 2025*