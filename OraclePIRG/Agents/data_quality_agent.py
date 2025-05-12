
from .base import Agent

class DataQualityAgent(Agent):
    def __init__(self):
        super().__init__("Data Quality Agent")

    def process(self, raw_data):
        return f"[DataQualityAgent] Data cleaned and validated."
