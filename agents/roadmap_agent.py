from langchain_core.prompts import ChatPromptTemplate
from . import llm
from models.schemas import LearningRoadmap


roadmap_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
        You are an AI Learning Roadmap Specialist.

        Create a realistic learning roadmap for the user's
        target career role.

        Divide the roadmap into sequential phases.
        Focus on practical learning and project development.
        Avoid repeating skills the user already knows.
        """
    ),
    (
        "human",
        """
        Target Role: {target_role}

        Existing Skills: {user_skills}

        Missing Skills: {missing_skills}

        Create a practical roadmap.
        """
    )
])

roadmap_chain = roadmap_prompt | llm.with_structured_output(
    LearningRoadmap
)


def roadmap_agent(state):
    print("\n[Roadmap Agent] Creating learning roadmap...")

    result = roadmap_chain.invoke({
        "target_role": state["target_role"],
        "user_skills": state["user_skills"],
        "missing_skills": state["skill_analysis"]["missing_skills"]
    })

    print("[Roadmap Agent] Roadmap completed.")

    return {
        "learning_roadmap": result.model_dump()
    }