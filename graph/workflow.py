
from typing import TypedDict, Any

from langgraph.graph import StateGraph, START, END

from agents.supervisor import supervisor_agent
from agents.skill_agent import skill_agent
from agents.project_agent import project_agent
from agents.roadmap_agent import roadmap_agent


class CareerState(TypedDict, total=False):
    user_request: str
    target_role: str
    user_skills: list[str]

    skill_analysis: dict[str, Any]
    project_recommendation: dict[str, Any]
    learning_roadmap: dict[str, Any]

    final_report: str


def aggregator_agent(state: CareerState):

    print("\n[Aggregator] Combining agent results...")

    skills = state["skill_analysis"]
    project = state["project_recommendation"]
    roadmap = state["learning_roadmap"]

    report = f"""
========================================
       AI CAREER ASSISTANT REPORT
========================================

TARGET ROLE:
{state['target_role']}

CURRENT SKILLS:
{', '.join(state['user_skills'])}

----------------------------------------
1. SKILL ANALYSIS
----------------------------------------

Existing Strengths:
{', '.join(skills['existing_strengths'])}

Missing Skills:
{', '.join(skills['missing_skills'])}

Priority Skills:
{', '.join(skills['priority_skills'])}

----------------------------------------
2. PROJECT RECOMMENDATION
----------------------------------------

Project Name:
{project['project_name']}

Description:
{project['project_description']}

Technologies:
{', '.join(project['technologies'])}

Difficulty:
{project['difficulty']}

----------------------------------------
3. LEARNING ROADMAP
----------------------------------------

Duration:
{roadmap['duration']}

Learning Phases:
{chr(10).join('- ' + phase for phase in roadmap['phases'])}

Final Goal:
{roadmap['final_goal']}

========================================
"""

    return {"final_report": report}


def build_graph():

    builder = StateGraph(CareerState)

    # Register agents
    builder.add_node("supervisor", supervisor_agent)
    builder.add_node("skill_agent", skill_agent)
    builder.add_node("project_agent", project_agent)
    builder.add_node("roadmap_agent", roadmap_agent)
    builder.add_node("aggregator", aggregator_agent)

    # Sequential execution
    builder.add_edge(START, "supervisor")
    builder.add_edge("supervisor", "skill_agent")

    # Both agents run after skill analysis is completed
    builder.add_edge("skill_agent", "project_agent")
    builder.add_edge("skill_agent", "roadmap_agent")

    # Aggregator waits for both agents
    builder.add_edge(
        ["project_agent", "roadmap_agent"],
        "aggregator"
    )

    builder.add_edge("aggregator", END)

    return builder.compile()
