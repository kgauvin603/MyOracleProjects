import asyncio
import nest_asyncio
from orchestrator import BetterBoyOrchestrator

# 🔁 Set this to "notebook" when in Jupyter, or "script" for standalone
RUN_MODE = "notebook"  # Change to "script" when deploying

# === Input Example ===
input_args = {
    "query": "Global Inflation 2025",
    "source": "Oracle + Reuters",
    "client_info": "Institutional Portfolio - ESG Bias",
    "diligence_packet": "PE Fund ABC Diligence Summary",
    "manager_data": "Manager DEF Performance YTD"
}

def run_orchestrator(args):
    orchestrator = BetterBoyOrchestrator()

    if RUN_MODE == "notebook":
        nest_asyncio.apply()
        return asyncio.get_event_loop().run_until_complete(
            orchestrator.run(**args)
        )
    else:
        return asyncio.run(orchestrator.run(**args))

# === Run and Print Output ===
if __name__ == "__main__":
    results = run_orchestrator(input_args)
    for r in results:
        print(r)
        
