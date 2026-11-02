from langchain_core.prompts import ChatPromptTemplate
from . import llm
from models.schemas import ProjectRecommendation


project_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
        You are an AI Project Recommendation Specialist.

        Recommend one practical portfolio project for the user's
        target career role.

        The project should:
        - Be suitable for a fresher.
        - Demonstrate relevant technical skills.
        - Help strengthen the user's portfolio.
        - Include a clear description and technologies.
        """
    ),
    (
        "human",
        """
        Target Role: {target_role}

        Existing Skills: {user_skills}

        Missing Skills: {missing_skills}
        """
    )
])

project_chain = project_prompt | llm.with_structured_output(
    ProjectRecommendation
)


def project_agent(state):
    print("\n[Project Agent] Generating project recommendation...")

    result = project_chain.invoke({
        "target_role": state["target_role"],
        "user_skills": state["user_skills"],
        "missing_skills": state["skill_analysis"]["missing_skills"]
    })

    print("[Project Agent] Recommendation completed.")

    return {
        "project_recommendation": result.model_dump()
    }