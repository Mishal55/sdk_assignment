from math_agent import math_agent
from general_agent import general_agent
from stream_handler import handle_stream

def run_agents(agents, input_text):
    for agent in agents:
        if agent.input_filter(input_text):
            handle_stream("agent_selected", agent.name)
            if "subtract" in input_text:
                from subtraction_schema import SubtractionInput
                input_data = SubtractionInput(minuend=10, subtrahend=3)
                result = agent.tools[0](input_data)
                handle_stream("result", f"{input_data.minuend} - {input_data.subtrahend} = {result}")
            else:
                handle_stream("response", "How can I assist you?")
            break

if __name__ == "__main__":
    user_input = input("Enter your query: ")
    run_agents([math_agent, general_agent], user_input)
