# 🤖 Multi-Agent AI Career Assistant

An AI-powered career guidance application built using **LangGraph, LangChain, Groq LLM, FastAPI, React, and Docker**. It uses multiple specialized AI agents to analyze a user's career goals, identify skill gaps, recommend projects, and generate a personalized learning roadmap.

🌐 **Live Application:** https://multiagent-career-frontend.onrender.com/

---

## 📌 Project Overview

Choosing the right career path and identifying the skills required to achieve it can be challenging. The Multi-Agent AI Career Assistant simplifies this process through an intelligent multi-agent workflow.

Users provide their target career role and existing technical skills. The application processes this information through specialized AI agents and generates a structured career development report.

### ✨ Key Features

- **Career Goal Analysis:** Identifies the user's desired career role.
- **Skill Gap Analysis:** Evaluates existing skills and identifies missing skills.
- **Project Recommendations:** Suggests practical projects based on the target role and skill gaps.
- **Personalized Learning Roadmap:** Generates a phased learning plan with an estimated duration.
- **Multi-Agent Architecture:** Uses specialized agents working together through LangGraph.
- **Structured AI Responses:** Uses Pydantic models to generate structured outputs.
- **Interactive Dashboard:** Provides a responsive React-based user interface.
- **REST API:** Exposes career analysis functionality through FastAPI.
- **Docker Support:** Containerizes the frontend and backend for deployment.

---

## 🏗️ System Architecture

The application follows a multi-agent architecture in which each agent performs a specialized task.

```text
                 USER
                   |
                   v
          React Frontend
                   |
                   v
             FastAPI
                   |
                   v
          LangGraph Workflow
                   |
                   v
           Supervisor Agent
                   |
                   v
             Skill Agent
                   |
             Skill Analysis
                   |
             +-----+-----+
             |           |
             v           v
        Project Agent  Roadmap Agent
             |           |
             v           v
       Project Ideas  Learning Plan
             |           |
             +-----+-----+
                   |
                   v
             Aggregator
                   |
                   v
           Final Career Report
                   |
                   v
             React Dashboard
```

### 🤖 Specialized AI Agents

| Agent | Responsibility |
|---|---|
| Supervisor Agent | Understands the user's career request and extracts the target role and existing skills. |
| Skill Agent | Identifies existing strengths, missing skills, and priority skills. |
| Project Agent | Recommends a relevant project based on the target role and skill gaps. |
| Roadmap Agent | Creates a structured learning roadmap. |
| Aggregator | Combines all agent outputs into a final career report. |

---

## 🛠️ Technology Stack

### Backend
- Python
- FastAPI
- LangChain
- LangGraph
- Groq LLM API
- Pydantic
- Uvicorn

### Frontend
- React.js
- Vite
- Tailwind CSS
- JavaScript
- Lucide React

### AI & Agent Frameworks
- Large Language Models (LLMs)
- Multi-Agent Systems
- Structured Output Generation
- Prompt Engineering
- LangGraph State Management

### Deployment & DevOps
- Docker
- Docker Compose
- Render
- Git
- GitHub

---

## 📂 Project Structure

```text
MultiAgentCareerAssistant/
│
├── agents/
│   ├── __init__.py
│   ├── supervisor.py
│   ├── skill_agent.py
│   ├── project_agent.py
│   └── roadmap_agent.py
│
├── graph/
│   └── workflow.py
│
├── models/
│   └── schemas.py
│
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── App.jsx
│   │   ├── App.css
│   │   ├── index.css
│   │   └── main.jsx
│   ├── Dockerfile
│   ├── package.json
│   └── vite.config.js
│
├── api.py
├── main.py
├── test_workflow.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .dockerignore
├── .gitignore
└── README.md
```

---

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/BhavaniLeela/MultiAgentCareerAssistant.git

cd MultiAgentCareerAssistant
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root directory.

```env
GROQ_API_KEY=your_groq_api_key
```

Get your API key from [Groq Console](https://console.groq.com/).

**Important:** Never upload your API key or `.env` file to GitHub.

### 5. Run the Backend

```bash
uvicorn api:app --reload
```

Backend URL:

```text
http://127.0.0.1:8000
```

API documentation:

```text
http://127.0.0.1:8000/docs
```

### 6. Run the Frontend

Open another terminal:

```bash
cd frontend
```

Install frontend dependencies:

```bash
npm install
```

Start the development server:

```bash
npm run dev
```

Frontend URL:

```text
http://localhost:5173
```

---

## 🐳 Running with Docker

The project supports Docker-based deployment using Docker Compose.

### Prerequisites

- Docker Desktop
- Docker Compose

### Build Docker Images

From the project root:

```bash
docker compose build
```

### Start the Application

```bash
docker compose up -d
```

### Check Running Containers

```bash
docker ps
```

### Access the Application

| Component | URL |
|---|---|
| Frontend | http://localhost:5173 |
| Backend API | http://localhost:8000 |
| API Documentation | http://localhost:8000/docs |

### Stop Containers

```bash
docker compose down
```

---

## 🔗 API Endpoints

The backend exposes REST API endpoints using FastAPI.

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Checks whether the API is running. |
| POST | `/career/analyze` | Generates a personalized career analysis. |
| GET | `/docs` | Opens interactive Swagger API documentation. |

### Example API Request

**POST** `/career/analyze`

Request body:

```json
{
  "user_request": "I want to become an AI Engineer. My existing skills are Python, SQL, Machine Learning, Deep Learning, RAG, LangChain and LangGraph."
}
```

### Example Response

```json
{
  "target_role": "AI Engineer",
  "final_report": "AI CAREER ASSISTANT REPORT..."
}
```

The final report contains:

1. Career Target Analysis
2. Existing Skills
3. Missing Skills
4. Priority Skills
5. Project Recommendations
6. Personalized Learning Roadmap

---

## ☁️ Deployment

The application is deployed using Render.

### Live Application

**Frontend:**

https://multiagent-career-frontend.onrender.com/

### Deployment Configuration

The frontend and backend are deployed as separate services.

**Backend Service**
- Runtime: Docker
- Dockerfile: `./Dockerfile`
- Docker build context: Repository root
- Environment variable: `GROQ_API_KEY`

**Frontend Service**
- Runtime: Static Site
- Root directory: `frontend`
- Build command: `npm install && npm run build`
- Publish directory: `dist`

Configure the frontend's API base URL to point to the deployed backend service. Add the deployed frontend origin to the backend's CORS `allow_origins` list.

---

## 🔐 Security Considerations

- API keys are stored using environment variables.
- `.env` is excluded from version control.
- Backend and frontend run as separate services.
- API requests are validated using Pydantic.
- Docker provides isolated application environments.

---

## 🎯 Learning Outcomes

This project demonstrates practical understanding of:

- Designing multi-agent AI systems.
- Building agent workflows using LangGraph.
- Integrating LLMs using LangChain and Groq.
- Generating structured outputs using Pydantic.
- Developing REST APIs using FastAPI.
- Building interactive interfaces using React.
- Containerizing applications using Docker.
- Deploying full-stack AI applications.

---

## 🚀 Future Enhancements

- Integrate RAG for context-aware career recommendations.
- Add user authentication and personalized profiles.
- Implement conversation memory.
- Integrate resume parsing and analysis.
- Add job description analysis and skill matching.
- Include progress tracking for learning roadmaps.
- Improve agent evaluation and response quality.
- Add persistent storage for user career reports.

---

## 👩‍💻 Author

**Bhavani Leela**

Computer Science and Engineering Graduate | Aspiring AI Engineer

- GitHub: https://github.com/BhavaniLeela
- Project Repository: https://github.com/BhavaniLeela/MultiAgentCareerAssistant

---

⭐ If you find this project interesting, consider giving the repository a star!

**Built with curiosity, experimentation, and a passion for Artificial Intelligence.**
