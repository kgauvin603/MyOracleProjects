from .base import Agent
from datetime import datetime
import json
import os
from reportlab.lib.pagesizes import LETTER
from reportlab.pdfgen import canvas

class ReportGenerator(Agent):
    def __init__(self):
        super().__init__("Report Generator Agent")

    def process(self, log_entries):
        timestamp = datetime.now().isoformat()
        text_report = f"=== Better Boy AI Report ===\nGenerated at: {timestamp}\n\n"

        structured_report = {
            "generated_at": timestamp,
            "entries": []
        }

        for entry in log_entries:
            text_report += f"{entry}\n\n"
            structured_report["entries"].append({"output": entry})

        text_report += "=== End of Report ===\n"

        # Save JSON (UTF-8 + emoji safe)
        json_filename = f"better_boy_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(json_filename, "w", encoding="utf-8") as f:
            json.dump(structured_report, f, indent=2, ensure_ascii=False)

        # Generate PDF using reportlab
        pdf_filename = f"better_boy_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
        c = canvas.Canvas(pdf_filename, pagesize=LETTER)
        width, height = LETTER

        c.setFont("Helvetica", 12)
        y = height - 40

        for line in text_report.splitlines():
            if not line.strip():
                y -= 14
                continue

            if y < 50:
                c.showPage()
                c.setFont("Helvetica", 12)
                y = height - 40

            c.drawString(40, y, line[:120])  # truncate long lines if needed
            y -= 14

        c.save()

        return {
            "text": text_report,
            "json_file": json_filename,
            "pdf_file": pdf_filename
        }
