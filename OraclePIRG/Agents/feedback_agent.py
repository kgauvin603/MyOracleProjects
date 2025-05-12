
from .base import Agent

class FeedbackAgent(Agent):
    def __init__(self):
        super().__init__("Feedback Agent")

    def process(self, report_data):
        simulated_feedback = "✅ Feedback captured: Client found the recommendations relevant and the explanations clear."
        return f"{report_data}\n\n[FeedbackAgent] {simulated_feedback}"
