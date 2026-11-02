from langchain_core.prompts import ChatPromptTemplate
from . import llm
from models.schemas import SkillAnalysis


skill_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
        You are a technical skill analysis specialist.

        Analyze the user's skills for the target career role.

        Identify:
        - Existing strengths.
        - Missing technical skills.
        - Priority skills to learn first.

        Be realistic and focus on industry-relevant skills.
        """
    ),
    (
        "human",
        """
        Target Role: {target_role}

        Existing Skills: {user_skills}
        """
    )
])

skill_chain = skill_prompt | llm.with_structured_output(
    SkillAnalysis
)


def skill_agent(state):
    print("\n[Skill Agent] Analyzing skill gaps...")

    result = skill_chain.invoke({
        "target_role": state["target_role"],
        "user_skills": state["user_skills"]
    })

    print("[Skill Agent] Analysis completed.")

    return {
        "skill_analysis": result.model_dump()
    }