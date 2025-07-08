Click below for the demo!!!!!!!!!!!!!!!!!!!!

[![Watch Demo](https://img.youtube.com/vi/tcF__KTex-s/hqdefault.jpg)](https://www.youtube.com/watch?v=tcF__KTex-s&list=PLe-YIIlt-fbO3hXVoaPK56ikWRT0A9Gzr&index=2)


# 📰 Website Content Summarizer using LangChain + Hugging Face 
This is a **lightweight Streamlit web app** that extracts and summarizes any public website’s content using **LangChain**, the **Hugging Face Inference API**, and **Mistral-7B**.

---

## ✨ Project Impact

In a world overflowing with information, this tool helps users **save time** by turning long-form website content into concise summaries — perfect for students, researchers, and professionals.

> "This is one of the most **practical AI utilities** I’ve built — it's simple, fast, and valuable."

---

## ⚙️ How It Works

1. Enter a public URL (like a blog post or news article)  
2. The app scrapes its readable content using `UnstructuredURLLoader`  
3. Sends it to the **Mistral-7B-Instruct** model via Hugging Face Inference API  
4. Summarizes the text using `LangChain`'s summarize chain  
5. Displays a clean, focused summary in seconds ⚡

---

## 🧠 Tech Stack

| Tool / Library         | Purpose                                 |
|------------------------|-----------------------------------------|
| 🦜 LangChain           | Summarization pipeline and prompt       |
| 🤗 Hugging Face Hub    | Hosting `Mistral-7B-Instruct` model     |
| 📰 Unstructured         | Extracts readable content from webpages |
| ✅ Validators           | Ensures input URL is valid              |
| 🧪 Streamlit            | Beautiful, interactive frontend         |

---

## 📁 Project Structure

```
📂 summarizer-huggingface/
├── app.py             # Streamlit application
├── .env               # Hugging Face token (not committed)
├── requirements.txt   # All dependencies
└── README.md
```

---

## 🔍 Example Use Case

> You come across a long 5,000-word research blog. Paste the URL into the app —  
> Within seconds, you get a **300-word summary** explaining everything. Boom. Done. ✅

---

## 📦 Installation & Setup

### 1️⃣ Clone the Repo

```bash
git clone https://github.com/jatinydav557/summarizer-hugging-face-langchain.git
cd summarizer-hugging-face-langchain
```

### 2️⃣ Create Virtual Environment

```bash
uv venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
uv pip install -r requirements.txt
```

### 3️⃣ Add `.env` file

```
HF_TOKEN=your_huggingface_api_key
```

Or paste the Hugging Face token directly into the sidebar when prompted.

---

## ▶️ Run the App

```bash
streamlit run app.py
```

Open your browser at: [http://localhost:8501](http://localhost:8501)

---

## 🧪 Requirements

```txt
streamlit
langchain
langchain-community
langchain-huggingface
validators
unstructured  # required to properly parse website HTML
```

> ⚠️ **Note**: The `unstructured` package is essential. If it gives errors, try:
> `pip install "unstructured[all-docs]"`

---

## 👨‍🎓 About Me

Hi, I'm **Jatin Yadav**, a final-year **MCA student** and passionate **Machine Learning Engineer**.  
I'm building **20+ real-world GenAI projects** to learn faster, contribute meaningfully, and land a great AI role.

> I don’t just follow tutorials — I build and deploy tools that solve real problems.

This summarizer app is a great example of how **LLMs can simplify knowledge digestion**.

📌 Open to roles in:
- 🧠 LLM / GenAI Engineering
- 🤖 NLP / RAG Systems
- ⚙️ MLOps & AI Tools

---

## 🧭 What's Next?

* [ ] Add multi-language support for websites  
* [ ] Merge with YouTube summarizer (multi-source RAG)  
* [ ] Deploy to Hugging Face Spaces / Streamlit Cloud

---

## 📢 Let’s Connect

- 🔗 [LinkedIn](https://www.linkedin.com/in/jatin557)  
- 💼 [GitHub](https://github.com/jatinydav557)  
- 📺 [YouTube Projects](https://www.youtube.com/@jatinML/playlists)  
- 📧 Email: jatinydav557@gmail.com  
- 📱 +91-7340386035

---

⭐ If you found this helpful, **give it a star** and share it with someone who reads a lot!

> "Summarization isn't just about compressing text. It's about saving lives in a world full of information overload."  
> – *You, the AI builder*

