# Q&A Chatbot using Retrieval-Augmented Generation (RAG)

## 📌 Project Description

This is a simple **Q&A chatbot** built using **Retrieval-Augmented Generation (RAG)**. The chatbot retrieves relevant information using embeddings and then generates answers using a **DeepSeek R1 model** via the **Groq API**. The project is implemented using the **LangChain framework** in Python.

## 🚀 Tech Stack

- **Python** (Recommended: 3.8+)
- **LangChain** (for RAG framework)
- **Ollama** (for creating embeddings)

## 🛠 Installation & Setup

Follow these steps to set up the chatbot on your local machine:

### **1. Fork the Repository**

Go to the GitHub repository page and click on the "Fork" button in the top right corner. This will create a copy of the repository in your GitHub account.

### **2. Clone the Repository**

```bash
git clone https://github.com/your-username/RAG-Chatbot.git
```

### **3. Create a Virtual Environment**

```bash
python -m venv myenv  # For Windows/Linux/Mac
source myenv/bin/activate  # Mac/Linux
myenv\Scripts\activate  # Windows
```

### **4. Install Dependencies**

```bash
pip install -r requirements.txt
```

### **5. Set Up Environment Variables**

Create a `.env` file in the root directory and add the following:

```ini
GROQ_API_KEY=your_groq_api_key
```

> **Note:** Never share your API key or commit it to GitHub.

### **6. Run the Chatbot**

```bash
streamlit run chatbot.py
```

## 📖 How It Works

1. **Indexing Phase:** The chatbot takes input from PDFs or other sources, splits the text into chunks, converts these chunks into embeddings using **Ollama**, and stores them in a **vector database**.
2. **Retrieval Phase:** The chatbot fetches relevant information from the vector database using **similarity search**. Retrieved information is then combined with the user’s query.
3. **Generation Phase:** The **DeepSeek R1 model** (via Groq API) generates a response.

## 🤝 Contributors

- **Md. Anwar Hossain Rana**
- **Md Shoaib Abdullah Khan**

---

**🚀 Happy Coding!**
