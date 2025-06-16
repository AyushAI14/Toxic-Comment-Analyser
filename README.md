# 🧠 Toxic Comment Analyzer

Analyze YouTube video comments and detect toxicity using a fine-tuned DistilBERT model, all wrapped in a FastAPI backend and a minimal frontend UI.

![Result Image](https://github.com/user-attachments/assets/e1eb2d7c-ade5-4810-a295-c5a29037cc8a)

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
├── notebook/                      # EDA, training notebooks
├── Dockerfile                     # For containerization
├── requirements.txt               # Python dependencies
├── config/config.yaml             # Configuration
├── main.py                        # Alternate CLI entrypoint
└── README.md                      # This file

---

## 🎯 Next Goals

- Dockerization
- CI/CD Integration
- Deployment

---
