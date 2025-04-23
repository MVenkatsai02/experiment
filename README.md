# 🤖 LLM-Based Retrieval-Augmented Generation (RAG) System

A smart AI-powered Retrieval-Augmented Generation (RAG) system that fetches relevant content from the internet, processes it, and generates answers using Google Gemini 1.5 Flash. Built with a Flask backend, Streamlit frontend, and powered by real-time web scraping and LLMs.

---

## 🛠️ Features

✅ Web search via Serper API  
✅ Intelligent article scraping and summarization  
✅ LLM-powered response generation using Gemini 1.5 Flash  
✅ Flask backend API for processing and generation  
✅ Streamlit UI for query input and response display  
✅ Easy deployment to Render (backend) and Streamlit Cloud (frontend)  

---

## 📂 Project Structure

```bash
experiment/
├── app.py              # Flask backend
├── utils.py            # Web search, scraping, LLM generation
├── frontend.py              # Streamlit frontend
├── requirements.txt        # Project dependencies
├── .env                    # API keys (excluded from Git)
├── .gitignore              # Ignore files
└── README.md               # Project documentation
```

## 🚀 Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/MVenkatsai02/experiment
cd multi-agent-ai-code-generator
```

### 2️⃣ Set Up a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 🔐 Environment Variables
 Create a .env file in the root directory:
 ```bash
GEMINI_API_KEY=your_gemini_1.5_flash_api_key
SERPER_API_KEY=your_serper_api_key
```

### 🧪 Running Locally
🔹 Run Flask Backend
```bash
python app.py
```
The backend will run at: http://localhost:5000/query

🔹 Run Streamlit Frontend
In another terminal:
```bash
streamlit run app.py
```
Streamlit UI will be available at: http://localhost:8501

### 🌍 Deployment
✅ Flask Backend on Render

1 Push the project to GitHub.

2 Go to Render.

3 Create a New Web Service → Select your repo.

4 Set:

    Build Command: pip install -r requirements.txt

    Start Command: python app.py

    Environment: Python 3

    Environment Variables:

        GEMINI_API_KEY

        SERPER_API_KEY

5 Deploy and get your backend URL:
Example: https://rag-backend.onrender.com/query

### ✅ Streamlit Frontend on Streamlit Cloud
1 Push the repo to GitHub (with updated backend URL in frontend app.py).

2 Go to Streamlit Cloud.

3 Deploy your repo and select streamlit_app/app.py as the main file.

4 Done! Share your app link.

### 💡 Example Usage
1 Open the deployed Streamlit app.

2 Enter a query like: AI in education.

3 View the LLM-generated response based on real-time web content.

### 🧰 Troubleshooting
💡 500 Error from API?
✔️ Check if GEMINI_API_KEY and SERPER_API_KEY are set in Render.

💡 CORS Error?
✔️ Add from flask_cors import CORS and CORS(app) in flask_app/app.py.

💡 Streamlit not receiving response?
✔️ Make sure you’re using the HTTPS Render URL in Streamlit code.


## 🛡️ License

This project is open-source under the MIT License.

## 📩 Contact & Contributions

🔹 Feel free to fork this repo & contribute!

🔹 Found a bug? Create an issue on GitHub.

🔹 Questions? Reach out via email: venkatsaimacha123@gmail.com

🚀 Built with ❤️ using Flask, Streamlit & Gemini AI 🚀

