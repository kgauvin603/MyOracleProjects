import asyncio
from agents.rag_agent import RAGAgent
from agents.data_ingestion_agent import DataIngestionAgent
from agents.data_quality_agent import DataQualityAgent
from agents.client_profiling_agent import ClientProfilingAgent
from agents.due_diligence_agent import DueDiligenceAgent
from agents.manager_evaluation_agent import ManagerEvaluationAgent
from agents.narrative_generation_agent import NarrativeGenerationAgent
from agents.accuracy_assurance_agent import AccuracyAssuranceAgent
from agents.personalization_agent import PersonalizationAgent
from agents.compliance_agent import ComplianceAgent
from agents.client_communication_agent import ClientCommunicationAgent
from agents.monitoring_agent import MonitoringAgent
from agents.explainability_agent import ExplainabilityAgent
from agents.feedback_agent import FeedbackAgent
from agents.report_generator import ReportGenerator

class BetterBoyOrchestrator:
    def __init__(self):
        self.agents = {
            "rag": RAGAgent(),
            "ingestion": DataIngestionAgent(),
            "quality": DataQualityAgent(),
            "profiling": ClientProfilingAgent(),
            "diligence": DueDiligenceAgent(),
            "manager": ManagerEvaluationAgent(),
            "narrative": NarrativeGenerationAgent(),
            "accuracy": AccuracyAssuranceAgent(),
            "personalization": PersonalizationAgent(),
            "compliance": ComplianceAgent(),
            "communication": ClientCommunicationAgent(),
            "monitoring": MonitoringAgent(),
            "explainability": ExplainabilityAgent(),
            "feedback": FeedbackAgent(),
            "report": ReportGenerator()
        }

    async def run_agent(self, agent, input_data):
        return agent.process(input_data)

    async def run(self, query, source, client_info, diligence_packet, manager_data, analyst_feedback=""):
        log = []

        tasks = [
            self.run_agent(self.agents["rag"], query),
            self.run_agent(self.agents["ingestion"], source),
            self.run_agent(self.agents["quality"], source),
            self.run_agent(self.agents["profiling"], client_info),
            self.run_agent(self.agents["diligence"], diligence_packet),
            self.run_agent(self.agents["manager"], manager_data)
        ]

        results = await asyncio.gather(*tasks)

        # ✅ Prevent string-splitting by appending results individually
        for result in results:
            log.append(result)

        # Sequential agents
        report = self.agents["narrative"].process(" ".join(results))
        log.append(report)

        checked = self.agents["accuracy"].process(report)
        log.append(checked)

        personalized = self.agents["personalization"].process(checked)
        log.append(personalized)

        compliant = self.agents["compliance"].process(personalized)
        log.append(compliant)

        delivered = self.agents["communication"].process(personalized)
        log.append(delivered)

        monitored = self.agents["monitoring"].process(log)
        log.append(monitored)

        # ✅ Flatten explainability output
        explained = self.agents["explainability"].process(log)
        if isinstance(explained, list):
            explained_text = "\n\n".join(str(item) for item in explained)
        else:
            explained_text = str(explained)
        log.append(explained_text)

        feedback = self.agents["feedback"].process(analyst_feedback)
        log.append(feedback)

        report_output = self.agents["report"].process(log)
        log.append(report_output)

        return log

if __name__ == "__main__":
    orchestrator = BetterBoyOrchestrator()
    results = asyncio.run(orchestrator.run(
        query="Global Inflation 2025",
        source="Oracle + Reuters",
        client_info="Family Office - Growth mandate",
        diligence_packet="XYZ Hedge Fund Data",
        manager_data="Manager Performance XYZ",
        analyst_feedback="Please emphasize downside risk next time"
    ))

    for result in results:
        print(result)

