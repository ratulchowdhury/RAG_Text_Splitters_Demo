from langchain_text_splitters import RecursiveCharacterTextSplitter, Language

splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.MARKDOWN,
    chunk_size=300,
    chunk_overlap=60)
text = """
            # 🌟 Awesome To-Do App

            A simple and elegant To-Do application built with **React** and **Power Automate** integration for seamless task tracking.

            ---

            ## 🚀 Features

            - ✨ Create, update, and delete tasks  
            - 📅 Set deadlines and reminders  
            - 🔄 Sync tasks with Microsoft To Do using Power Automate  
            - 📊 View daily productivity stats  

            ---

            ## 🧰 Tech Stack

            | Layer | Technology |
            |-------|-------------|
            | Frontend | React + Tailwind CSS |
            | Backend | Power Automate Flows |
            | Database | Dataverse |
            | Auth | Microsoft Entra ID (Azure AD) |

            ---

            ## ⚙️ Setup Instructions

            1. Clone the repository  
            ```bash
            git clone https://github.com/yourusername/awesome-todo.git

    """
    
chunks = splitter.split_text(text)
print(f"First Chunk Content: {chunks[0]}")  
print(f"Total Chunks Created: {len(chunks)}")