
from .base import Agent

class RAGAgent(Agent):
    def __init__(self):
        super().__init__("RAG Agent")

    def process(self, query):
        return f"[RAGAgent] Retrieved data for query: {query}"
