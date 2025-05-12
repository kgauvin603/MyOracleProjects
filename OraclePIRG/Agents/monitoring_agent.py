
from .base import Agent

class MonitoringAgent(Agent):
    def __init__(self):
        super().__init__("Monitoring Agent")

    def process(self, activity_log):
        return f"[MonitoringAgent] Monitored and logged process activity."
