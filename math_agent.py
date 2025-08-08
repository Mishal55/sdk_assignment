from agent import Agent
from subtraction_tool import subtract_numbers

math_agent = Agent(
    name="MathAgent",
    tools=[subtract_numbers],
    input_filter=lambda input: "subtract" in input.lower()
)
