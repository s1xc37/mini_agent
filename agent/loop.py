from llm.llm_client import send_message, check_model
from agent.state import create_initial_state
from llm.payload_builder import build_payload
from agent.handler import handle_action
from agent.planning import make_plan

import json
# Load system_executor prompt
def load_system(path):
    with open(path, "r") as f:
        system_prompt = f.readlines()
    return system_prompt


def clean_json(text):
    text = text.strip()

    if text.startswith("```"):
        text = text.split("```")[1]

    return text.strip()

def safe_parse(text):
    try:
        return json.loads(text)
    except:
        cleaned = clean_json(text)
        return json.loads(cleaned)

def execute_step(step, payload):
    step_message = create_initial_state("user", step)[0]
    payload["messages"].append(step_message)

    llm_response = send_message(payload)

    payload["messages"].append({
        "role": "assistant",
        "content": llm_response
    })

    print(llm_response)

    try:
        parsed = safe_parse(llm_response)
        res = handle_action(parsed)
        if res:
            payload["messages"].append(res)
    except Exception as e:
        print("ERROR:", e)
        print("RAW:", repr(llm_response))

system_prompt = load_system(path="./agent/prompts/system.txt")

system_message = create_initial_state("system", system_prompt, is_json_format=False)
payload = build_payload(system_message)

def run_agent():

    print("Hello! im your personal coding agent ;)")
    try:
        print(f"model is alive?: {check_model()}\n")
    except:
        print("Server does not respond")
    while True:

        m_input = input(">>> ")
        plan = make_plan(m_input)
        try:
            plan_parsed = safe_parse(plan)
        except Exception as e:
            print("ERROR:", e)
            print("RAW:", repr(plan))
            continue

        message = {
            "role": "user",
            "content": f"goal is {plan_parsed['goal']}"
        }

        payload["messages"].append(message)

        for step in plan_parsed["plan"]:
            execute_step(step, payload)
