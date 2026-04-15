from llm.llm_client import send_message, check_model
from agent.state import create_initial_state
from llm.payload_builder import build_payload
from agent.handler import handle_action

import json

messages = create_initial_state()
payload = build_payload(messages)

def run_agent():
    print("Hello! im your personal coding agent ;)")
    print(f"model is alive?: {check_model()}\n")
    while True:
        m_input = input(">>> ")
        message = {
            "role": "user",
            "content": m_input
        }
        payload["messages"].append(message)
        llm_response = send_message(payload)
        payload["messages"].append({
            "role": "assistant",
            "content": llm_response
        })
        llm_response = llm_response.strip()
        try:
            parsed = json.loads(llm_response)
            res = handle_action(parsed)
            if res:
                payload["messages"].append(res)
        except Exception as e:
            print("ERROR:", e)
            print("RAW:", repr(llm_response))
            continue
        # print(llm_response)

