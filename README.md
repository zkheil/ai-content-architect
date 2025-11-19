#  AI Content Architect (Full-Stack GenAI Assistant)

> A local, privacy-focused AI content generator built with **FastAPI**, **React**, and a fine-tuned **T5 Transformer** model.

![Backend](https://img.shields.io/badge/Backend-FastAPI-green) ![Frontend](https://img.shields.io/badge/Frontend-React_Vite-blue) ![AI Model](https://img.shields.io/badge/Model-T5_Small-orange)

---

##  About The Project
Most AI writing tools rely on expensive external APIs (like OpenAI). **AI Content Architect** is different. It runs a **fine-tuned T5-Small model entirely locally**, allowing users to generate creative content (quotes, summaries, and blog titles) with **zero latency** and **zero cost**.

This project bridges the gap between **Machine Learning** and **Full-Stack Engineering**, demonstrating how to serve heavy AI models via a lightweight REST API to a modern frontend.

###  Key Features
* **Multi-Mode Generation:** Capable of generating **Quotes**, **Summaries**, and **Creative Titles** based on user prompts.
* **Local Inference:** Runs the T5 model on the CPU/GPU without making external API calls.
* **FastAPI Backend:** High-performance asynchronous API documentation (Swagger UI) enabled.
* **Modern Frontend:** Built with React and Vite for a lightning-fast, responsive user experience.

---

##  Tech Stack

### Backend (The Brain)
* **Framework:** FastAPI (Python)
* **ML Library:** Hugging Face Transformers & PyTorch
* **Model:** T5-Small (Fine-tuned for text-to-text generation)

### Frontend (The Interface)
* **Framework:** React.js (Vite)
* **Styling:** CSS Modules / Tailwind (depending on your implementation)
* **State Management:** React Hooks (useState, useEffect)

---

##  System Architecture

The application follows a strict **Client-Server** architecture:

1.  **The React Client:** Captures user prompts and desired content type (e.g., "Generate a quote about Success").
2.  **The API Layer:** Sends an asynchronous `POST` request to the FastAPI backend.
3.  **The Inference Engine:**
    * The backend receives the text.
    * It creates a specific prompt prefix (e.g., `summarize: ...`).
    * It feeds the text into the loaded **T5 Tokenizer** and **Model**.
    * It decodes the generated tokens back into human-readable text.
4.  **The Response:** The generated content is sent back as a JSON response to be displayed on the UI.

---

##  How to Run Locally

### Prerequisites
* Python 3.8+
* Node.js & npm

### 1. Clone the Repository
```bash
git clone [https://github.com/SaravanaKumar056/ai-content-architect.git](https://github.com/SaravanaKumar056/ai-content-architect.git)
cd ai-content-architect
2. Backend Setup (FastAPI)
Bash

# Navigate to backend folder
cd backend

# Install Python dependencies
pip install fastapi uvicorn transformers torch

# Start the API Server
uvicorn main:app --reload
# Server will start at http://localhost:8000
3. Frontend Setup (React)
Bash

# Open a new terminal and navigate to frontend folder
cd frontend

# Install dependencies
npm install

# Start the React Dev Server
npm run dev
# Client will start at http://localhost:5173
 Future Scope
Model Quantization: Implement ONNX runtime to make the model faster and lighter.

Database Integration: Add MongoDB to save user generation history.

Docker Support: Containerize the Frontend and Backend for one-click deployment.

 Author
Saravanakumar B

LinkedIn

GitHub


---

### 2. The GitHub "About" Section (Sidebar)

This is crucial because your project involves both Python and JavaScript. You need to use keywords that highlight the **AI** aspect so recruiters don't skip it.

**Description:**
> A full-stack AI content generator built with FastAPI and React. Runs a fine-tuned T5 Transformer model locally to generate quotes, summaries, and titles without external APIs.

**Topics (Tags):**
`generative-ai` `fastapi` `react` `machine-learning` `nlp` `transformers` `full-stack` `t5-model` `python` `vite`

**Paste these into your repository settings immediately.** It looks very impressive.
