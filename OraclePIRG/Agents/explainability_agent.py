
from .base import Agent

class ExplainabilityAgent(Agent):
    def __init__(self):
        super().__init__("Explainability Agent")

    def process(self, report_data):
        explanation = "[ExplainabilityAgent] Provided explanation of agent decisions and insights rationale."
        return f"{report_data}\n\n{explanation}"
