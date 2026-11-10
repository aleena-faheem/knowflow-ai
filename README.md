
# KnowFlow AI 🧠

An AI-powered knowledge assistant that transforms documents
into searchable knowledge and provides context-aware answers
with verifiable source citations.

## Overview

KnowFlow AI is a Retrieval-Augmented Generation (RAG)
application designed to help users interact with their
documents using natural language.

## Current Features

- FastAPI backend
- Streamlit dashboard
- SQLite database
- Document, conversation and message data models
- Dashboard statistics API
- Health monitoring endpoint
- Multi-page application navigation

## Technology Stack

| Component | Technology |
|---|---|
| Frontend | Streamlit |
| Backend | FastAPI |
| Language | Python |
| Database | SQLite |
| ORM | SQLAlchemy |
| API Server | Uvicorn |

## Architecture

Streamlit Frontend
       |
       v
FastAPI Backend
       |
       v
Service Layer
       |
       v
SQLite Database

## Project Structure

knowflow-ai/
├── backend/
├── frontend/
├── tests/
├── storage/
├── docs/
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md

## Setup Instructions

### 1. Clone the repository

git clone https://github.com/aleena-faheem/knowflow-ai.git

cd knowflow-ai

### 2. Create a virtual environment

python -m venv venv

### 3. Activate it on Windows

.\venv\Scripts\Activate.ps1

### 4. Install dependencies

pip install -r requirements.txt

### 5. Run the backend

uvicorn backend.app.main:app --reload

Backend documentation:
http://localhost:8000/docs

### 6. Run the frontend

Open a second terminal:

streamlit run frontend/app.py

Frontend:
http://localhost:8501

## Roadmap

- [ ] Document upload and extraction
- [ ] Text cleaning and chunking
- [ ] Sentence Transformers embeddings
- [ ] ChromaDB vector storage
- [ ] Semantic search and retrieval
- [ ] Gemini-powered RAG responses
- [ ] Citation validation and abstention
- [ ] Conversation history
- [ ] Document comparison
- [ ] RAG evaluation dashboard
- [ ] Docker deployment

## Project Status

Under active development.

## Author

Aleena Faheem
