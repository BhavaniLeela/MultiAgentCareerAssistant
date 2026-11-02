from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
import traceback

from graph.workflow import build_graph


app = FastAPI(
    title="Multi-Agent AI Career Assistant",
    description="AI-powered career guidance using LangGraph multi-agent workflow",
    version="1.0.0"
)


# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "https://multiagent-career-frontend.onrender.com"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Initialize multi-agent workflow
career_graph = build_graph()


# Request schema
class CareerRequest(BaseModel):
    user_request: str = Field(
        min_length=10,
        description="User's career goal and existing skills"
    )


# Response schema
class CareerResponse(BaseModel):
    target_role: str
    final_report: str


# Health check
@app.get("/")
def home():
    return {
        "message": "Multi-Agent AI Career Assistant API is running!",
        "status": "healthy"
    }


# Career analysis
@app.post("/career/analyze", response_model=CareerResponse)
def analyze_career(request: CareerRequest):
    try:
        result = career_graph.invoke(
            {"user_request": request.user_request},
            config={"recursion_limit": 15}
        )

        return CareerResponse(
            target_role=result["target_role"],
            final_report=result["final_report"]
        )

    except Exception:
        print("\n========== CAREER ANALYSIS ERROR ==========")
        traceback.print_exc()
        print("===========================================\n")

        raise HTTPException(
            status_code=500,
            detail="Career analysis failed. Please check backend logs."
        )