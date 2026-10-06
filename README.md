# 🧠 Self-Learning AI Agent

A production-quality, framework-free **Self-Learning AI Agent** built in Python, FastAPI, Streamlit, and SQLite. The agent features goal understanding, context minimization, isolated vector RAG retrieval, safe AST tool calling, self-evaluation monitoring, and cross-conversation experience learning.

---

## ❓ Problem Statement

Standard conversational AI chatbots operate statelessly across sessions. When a user provides explicit preferences or corrective feedback (e.g. *"Your explanations are too complicated; use simple real-world analogies"*), traditional chatbots fail to store this experience or adapt future responses in new conversations.

---

## 💡 Solution

This system introduces a persistent **Self-Learning Loop** without requiring complex neural-network retraining or fine-tuning:
1. **Planner Intent Router**: Categorizes user requests to minimize context window overhead.
2. **Memory & RAG Engines**: Manages short-term conversation sessions, long-term user facts, and session-isolated document vector search.
3. **Self-Evaluation Monitor**: Evaluates generated responses against relevance, correctness, completeness, and context grounding (`0-100` score), triggering retries on low scores.
4. **User Feedback Integration**: Captures explicit user guidance comments and records them as structured problem-solving experiences in SQLite.
5. **Cross-Conversation Strategy Adaptation**: Automatically retrieves past negative feedback lessons in new sessions to adapt response strategies.

---

## 🏗️ Architecture

```
User Prompt
    │
    ▼
FastAPI REST API / Streamlit Dashboard
    │
    ▼
SelfLearningAgent (Orchestration Loop)
    │
    ├──► AgentPlanner (Intent Routing & Past Lesson Retrieval)
    │
    ├──► MemoryDatabase (SQLite Short/Long-Term Facts & Experiences)
    │
    ├──► RAGEngine (Document Chunking & Vector Similarity Search)
    │
    ├──► Safe Tool Registry (AST Math Calculator & Memory Tools)
    │
    ▼
LLM Client Synthesis (OpenAI format with Mock Fallback)
    │
    ▼
AgentEvaluator (Relevance, Correctness & Grounding Audit)
    │
    ├──► Score < 70? ──► Trigger Self-Improvement Retry Loop
    │
    ▼
User Feedback Submission (Thumbs Up/Down & Comments)
    │
    ▼
Learning Experience Record Persistent Storage ──► Adapted Future Strategy
```

---

## ✨ Features

- **Goal Understanding & Intent Routing**: Dynamically classifies queries into `GENERAL_KNOWLEDGE`, `CALCULATION`, `DOCUMENT_QUESTION`, `DOCUMENT_SUMMARY`, `MEMORY_QUERY`, `MEMORY_SAVE`, `IMAGE_QUESTION`, or `NORMAL_CHAT`.
- **Parallel Tool Calling**: Secure AST-based math evaluation (`calculator`), long-term fact storage (`memory_save`), and memory search (`memory_search`).
- **Knowledge RAG System**: PDF, TXT, and Markdown ingestion with TF-IDF/Vector similarity search and active document session isolation.
- **Objective Self-Evaluation & Retry**: Automated scoring (`0-100`) with iterative refining retries.
- **Feedback-Based Self-Learning**: Stores experience lessons from user feedback and retrieves them to adapt reasoning in future conversations.
- **Prompt Leakage & Security Guards**: Sanitizes outputs to prevent system prompts, instructions, or internal keys from leaking into responses.

---

## 🛠️ Tech Stack

- **Core Language**: Python 3.13+
- **REST API**: FastAPI + Uvicorn
- **Frontend UI**: Streamlit
- **Database / Vector Search**: SQLite3 + NumPy
- **LLM Integration**: OpenAI SDK (compatible with OpenAI, Gemini, Groq) + Rule-based mock fallback
- **Testing Framework**: pytest + pytest-asyncio
- **Version Control**: Git / GitHub

---

## 🚀 Installation & Setup (Windows)

### 1. Clone Repository
```powershell
git clone https://github.com/your-username/SL-AI-agent.git
cd SL-AI-agent
```

### 2. Create and Activate Virtual Environment
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 3. Install Dependencies
```powershell
pip install -r requirements.txt
```

---

## 🔐 Environment Variables Configuration

Copy `.env.example` to `.env`:
```powershell
copy .env.example .env
```

Configure your environment settings in `.env`:
```ini
# LLM Provider: openai, gemini, groq, or mock
LLM_PROVIDER=openai
OPENAI_API_KEY=your_actual_api_key_here
OPENAI_MODEL=gpt-4o-mini
OPENAI_BASE_URL=https://api.openai.com/v1

# Paths
DB_PATH=data/agent.db
LOG_PATH=logs/agent.log
KNOWLEDGE_DIR=knowledge
```

---

## 🏃 Running the Application

### 1. Start FastAPI REST Backend
```powershell
.venv\Scripts\python main.py
```
*API running at `http://127.0.0.1:8000` | Swagger Docs at `http://127.0.0.1:8000/docs`*

### 2. Start Streamlit Frontend Dashboard
```powershell
.venv\Scripts\streamlit run frontend/app.py
```
*Dashboard opens at `http://localhost:8501`*

---

## 📡 API Endpoints Reference

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/` | Root endpoint displaying system operational status |
| `GET` | `/health` | Health check endpoint returning version & provider status |
| `POST` | `/chat` | Executes the complete agent reasoning & evaluation loop |
| `POST` | `/feedback` | Records user ratings and updates self-learning experience DB |
| `POST` | `/documents` | Uploads and indexes PDF/TXT/MD files into RAG storage |
| `GET` | `/memory` | Retrieves stored long-term facts and learning experiences |
| `GET` | `/logs` | Tails recent lines from the application log file |

---

## 🔄 Example Self-Learning Workflow

1. **Conversation 1**: User asks *"Explain recursion to a beginner."* Agent provides a technical explanation.
2. **User Feedback**: User submits negative feedback: *"Too complicated. Use a very simple real-world analogy."*
3. **Experience Persistence**: System records feedback lesson in `learning_experiences` table.
4. **Conversation 2 (New Session)**: User asks *"Explain binary search to me."*
5. **Strategy Adaptation**: Agent retrieves past negative feedback lesson, sets trace steps `Retrieved relevant learning experience` → `Adapted strategy`, and generates answer using a real-world dictionary lookup analogy.

---

## 🧪 Testing

Run the full pytest suite:
```powershell
.venv\Scripts\pytest -v
```

### Verified Test Suite Metrics:
- **Total Test Files**: 17
- **Total Collected Tests**: 69
- **Passed**: 69
- **Failed**: 0
- **Skipped**: 0

---

## ⚠️ Explicit Project Limitations

- **No Neural-Network Retraining**: The system does NOT retrain or fine-tune neural network weights.
- **Self-Learning Scope**: Self-learning is achieved purely through persistent experience logging, memory retrieval, prompt instruction adaptation, and user feedback integration.
