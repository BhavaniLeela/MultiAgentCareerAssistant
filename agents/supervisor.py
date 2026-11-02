
from typing import TypedDict

from langchain_core.prompts import ChatPromptTemplate
from agents import llm


class UserProfile(TypedDict):
    target_role: str
    user_skills: list[str]


supervisor_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
        You are an AI Career Supervisor.

        Analyze the user's career request.

        Identify:
        1. Target career role.
        2. Skills the user already knows.

        Return a clear, concise user profile.
        Do not invent skills that the user has not mentioned.
        """
    ),
    ("human", "{request}")
])

supervisor_chain = supervisor_prompt | llm.with_structured_output(
    UserProfile
)


def supervisor_agent(state):
    print("\n[Supervisor] Analyzing user request...")

    result = supervisor_chain.invoke({
        "request": state["user_request"]
    })

    print("[Supervisor] Target role:", result["target_role"])

    return {
        "target_role": result["target_role"],
        "user_skills": result["user_skills"]
    }
