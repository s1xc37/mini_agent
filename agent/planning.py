from llm.llm_client import send_message
from agent.state import create_initial_state
from llm.payload_builder import build_payload

def make_plan(message):
    with open("./agent/prompts/planning_system.txt", "r") as f:
        lines = f.readlines()
    payload = build_payload(
        [
            {
            "role": "system",
            "content": "".join(lines),
            },
            {
                "role": "user",
                "content": message,
            }
        ]
    )
    plan_data = send_message(payload).strip()
    return plan_data
