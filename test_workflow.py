
import traceback
from graph.workflow import build_graph

print("Building career graph...")

career_graph = build_graph()

print("Career graph created successfully!")

test_input = {
    "user_request": """
    My target career role is AI Engineer.

    My existing technical skills are Python and Machine Learning.

    Analyze my skills, recommend a project,
    and create a learning roadmap.
    """
}

try:
    print("\nStarting multi-agent workflow...")

    result = career_graph.invoke(
        test_input,
        config={"recursion_limit": 15}
    )

    print("\n========== FINAL CAREER REPORT ==========")
    print(result["final_report"])
    print("\nWorkflow completed successfully!")

except Exception:
    print("\n========== WORKFLOW ERROR ==========")
    traceback.print_exc()
