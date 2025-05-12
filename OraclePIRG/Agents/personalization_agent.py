
from .base import Agent

class PersonalizationAgent(Agent):
    def __init__(self):
        super().__init__("Personalization Agent")

    def process(self, report_content):
        return f"[PersonalizationAgent] Personalized report based on client profile."
