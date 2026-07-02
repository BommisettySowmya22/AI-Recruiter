# AI Recruiter – Intelligent Candidate Ranking

## Overview
This project is an AI-powered recruitment system built for the Redrob Data & AI Challenge.

Instead of matching keywords, it understands candidate profiles using semantic embeddings and ranks candidates using hybrid scoring.

## Features
- Semantic search using Sentence Transformers
- FAISS vector search
- Hybrid candidate ranking
- Behavioral signal scoring
- Explainable recommendations
- Submission file generation
- Validator-compatible output

## Tech Stack
- Python
- Sentence Transformers
- FAISS
- Scikit-learn
- Pandas
- NumPy

## Project Structure

AI_RECRUITER/
├── data/
├── outputs/
├── src/
├── main.py
├── requirements.txt
└── README.md

## Run

pip install -r requirements.txt

python main.py

## Output

outputs/submission.csv
