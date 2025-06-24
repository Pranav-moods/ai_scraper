# ai_scraper

This project implements an end-to-end intelligent pipeline for rewriting, reviewing, and storing book chapters using AI, with reinforcement-learning-based retrieval for future reuse and publication.

## 🔧 Features
- ** Scraper** - Scrapes or loads raw chapter content along with screen shot
-  **AI Writer** – Modernizes and rewrites raw book chapters using Gemini.
-  **AI Reviewer** – Enhances clarity, grammar, and structure.
-  **Human-in-the-loop Editing** – Editable review round before finalization.
-  **Storage with ChromaDB** – Stores and versions final chapters with metadata.
-  **RL-Based Search** – Retrieves best-matching chapters using a reward-based algorithm.

-  ### 🔨 Requirements

- Python 3.10+
- [Gemini API Access](https://ai.google.dev/)
- `chromadb`  
Install dependencies:
```bash
pip install chromadb

## 📦 Directory Structure
.
├── 1_scraper.py               # For scraping chapter text
├── 2_ai_writer_and_review.py  # AI rewrite + review + human edit
├── 3_human_edit_round_1.txt   # Manual editing interface
├── 4_storage.py               # Save final chapter to ChromaDB
├── 5_view_storage.py          #  View all saved chapters
├── 6_rl.py                    # RL-based chapter search          
├── final_version.txt          # Final edited chapter
├── ch1.txt                    # Original chapter input
├── llm_utils.py               # Gemini API helper
├── main.py                    # Scraper helper
└── README.md

🚀 How to Use

1. Clone the Repository
2. Install Dependencies
3. Add Gemini API Access

## Steps to Configure Your API Key
--Get your API key from Google AI Studio.
--in llm_utils.py replace "your_google_gemini_api_key_here" with your actual API key

4. Run the Scraper,AI Rewrite and Review & Human Edit
5. Store Final Version
6.View Saved Chapters
7.Perform RL-Based Search
