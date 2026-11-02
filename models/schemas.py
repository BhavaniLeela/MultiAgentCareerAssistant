from pydantic import BaseModel, Field


class SkillAnalysis(BaseModel):
    existing_strengths: list[str] = Field(
        description="Skills the user already knows"
    )

    missing_skills: list[str] = Field(
        description="Skills needed for the target role"
    )

    priority_skills: list[str] = Field(
        description="Most important skills to learn first"
    )


class ProjectRecommendation(BaseModel):
    project_name: str
    project_description: str
    technologies: list[str]
    difficulty: str


class LearningRoadmap(BaseModel):
    duration: str
    phases: list[str]
    final_goal: str