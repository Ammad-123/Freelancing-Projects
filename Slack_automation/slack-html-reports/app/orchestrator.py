from app.slack_client import SlackService
from app.report_generator import HTMLReport

class ReportOrchestrator:
    def run(self):
        # Example data (can be AI, analytics, DB, APIs)
        report_data = {
            "total_users": 1200,
            "errors": 3,
            "conversion_rate": "4.8%"
        }

        generator = HTMLReport()
        report_path = generator.generate(report_data)

        slack = SlackService()
        slack.send_message("✅ New automated HTML report generated")
        slack.upload_html(report_path)
