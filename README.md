# 🧠 Toxic Comment Analyzer

Analyze YouTube video comments and detect toxicity using a fine-tuned DistilBERT model, all wrapped in a FastAPI backend and a minimal frontend UI.

![Image](https://github.com/user-attachments/assets/f986cbdb-b0e3-44a3-a0f9-c17938194cfd)
---

## 🚀 Features

- 🔎 Scrapes YouTube comments using a given video URL
- ✨ Cleans and processes text using custom pipelines
- 🤖 Predicts toxicity using `martin-ha/toxic-comment-model` (DistilBERT)
- 📊 Shows percentage of toxic/non-toxic comments + average confidence
- 🖥️ Simple frontend with HTML+CSS and a loading spinner
- 📁 MLOps-structured project with modular components
- 🐳 Dockerization

---

## 🛠 Tech Stack

- Python
- FastAPI
- HuggingFace Transformers (`distilbert-toxic-model`)
- PyTorch
- HTML + CSS
- Jinja2 (for rendering)
- Logging & YAML Configs
- Docker
- Deployment app in EC2
- CI/CD Integration
---

## 📂 Project Structure

```bash
.
├── app.py                          # FastAPI entrypoint
├── templates/index.html           # Frontend template
├── src/                           # ML pipeline modules
├── artifacts/                     # Stored artifacts
├── notebook/                      # EDA, training notebooks
├── Dockerfile                     # For containerization
├── requirements.txt               # Python dependencies
├── config/config.yaml             # Configuration
├── main.py                        # Alternate CLI entrypoint
└── README.md                      # This file

```

