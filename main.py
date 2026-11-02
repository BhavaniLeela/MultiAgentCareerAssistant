from graph.workflow import build_graph


def main():

    print("\n================================")
    print("     AI CAREER ASSISTANT")
    print("================================")

    user_request = input(
        "\nDescribe your career goal and existing skills:\n> "
    ).strip()

    if not user_request:
        print("Please enter your career request.")
        return

    graph = build_graph()

    initial_state = {
        "user_request": user_request
    }

    print("\nStarting Multi-Agent Workflow...")

    result = graph.invoke(
        initial_state,
        config={"recursion_limit": 15}
    )

    print(result["final_report"])


if __name__ == "__main__":
    main()