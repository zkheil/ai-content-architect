Hybrid AI Content Architect

Engineering Goal: Minimize inference costs and latency by implementing a tiered architecture that routes requests between a distilled local model and a Large Language Model (LLM) API.

🏗️ System Architecture

The core innovation in this project is the Intelligent Routing Engine, which decides where to process data based on complexity.

graph TD
    User[React Client] -->|POST Request| API[FastAPI Gateway]
    API -->|Analyze Complexity| Router{Routing Logic}
    
    Router -->|Simple/Short| Local[Local T5-Small Model]
    Router -->|Complex/Creative| Cloud[Gemini Flash API]
    
    Local -->|Result| Response
    Cloud -->|Result| Response
    
    subgraph Edge Compute [Laptop / CPU]
    Local
    end
    
    subgraph Cloud Tier [Google Cloud]
    Cloud
    end


🚀 Key Features

1. Cost-Optimized Inference

Local-First Strategy: 70% of requests (captions, simple summaries) are handled by a fine-tuned T5-Small (60M params) model running on-device (CPU).

Zero Latency Cost: Local inference averages 120ms vs 800ms+ for cloud roundtrips.

2. Cloud Fallback & Escalation

Requests requiring "Creativity" (Hashtags) or "Deep Context" (Long summaries) automatically escalate to Google Gemini 2.5 Flash.

Fail-safe implemented: If local inference fails, the system silently falls back to cloud.

🛠️ Tech Stack

Model Training: PyTorch, HuggingFace Trainer (Fine-tuned on Colab T4).

Backend: FastAPI, Uvicorn (Async implementation).

Frontend: React + Vite, Tailwind CSS.

External API: Google Gemini (Generative Language API).

💻 Setup & Run

Clone Repo

git clone [https://github.com/yourname/ai-content-architect.git](https://github.com/yourname/ai-content-architect.git)


Backend Setup

Place your fine-tuned T5 model in backend/local_model.

Add your API Key in main.py.

cd backend
pip install -r requirements.txt
uvicorn main:app --reload


Frontend Setup

cd frontend
npm install
npm run dev


📈 Performance Metrics

Metric

Local T5

Gemini Cloud

Latency

~150ms

~900ms

Cost

$0.00

API Rate

Privacy

100% Local

Data sent to Cloud

Developed by Saravanakumar | Focus: Scalable ML Systems & Full Stack Engineering