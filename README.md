# 🧠 Toxic Comment Analyzer

Analyze YouTube video comments and detect toxicity using a fine-tuned DistilBERT model, all wrapped in a FastAPI backend and a minimal frontend UI.

![Result Screenshot](./aaf6a21d-1dae-4cca-9d37-052d6f8d25bf.png)

---

## 🚀 Features

- 🔎 Scrapes YouTube comments using a given video URL
- ✨ Cleans and processes text using custom pipelines
- 🤖 Predicts toxicity using `martin-ha/toxic-comment-model` (DistilBERT)
- 📊 Shows percentage of toxic/non-toxic comments + average confidence
- 🖥️ Simple frontend with HTML+CSS and a loading spinner
- 📁 MLOps-structured project with modular components
- 🐳 Docker-ready

---

## 🛠 Tech Stack

- FastAPI
- HuggingFace Transformers (`distilbert-toxic-model`)
- PyTorch
- HTML + CSS
- Jinja2 (for rendering)
- Logging & YAML Configs
- Docker

---

## 📂 Project Structure

```bash
.
├── app.py                          # FastAPI entrypoint
├── templates/index.html           # Frontend template
├── src/                           # ML pipeline modules
├── artifacts/                     # Stored artifacts
├── distilbert-toxic-model-v1/     # Pretrained model files
├── notebook/                      # EDA, training notebooks
├── Dockerfile                     # For containerization
├── requirements.txt               # Python dependencies
├── config/config.yaml             # Configuration
├── main.py                        # Alternate CLI entrypoint
└── README.md                      # This file
