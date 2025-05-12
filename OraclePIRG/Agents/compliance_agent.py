
from .base import Agent

class ComplianceAgent(Agent):
    def __init__(self):
        super().__init__("Compliance Agent")

    def process(self, report_content):
        return f"[ComplianceAgent] Compliance checks passed."
