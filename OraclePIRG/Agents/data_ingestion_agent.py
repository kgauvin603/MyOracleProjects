
from .base import Agent

class DataIngestionAgent(Agent):
    def __init__(self):
        super().__init__("Data Ingestion Agent")

    def process(self, source_info):
        return f"[DataIngestionAgent] Data ingested from {source_info}"
