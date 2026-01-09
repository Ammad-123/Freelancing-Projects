from jinja2 import Environment, FileSystemLoader
from datetime import datetime

class HTMLReport:
    def __init__(self):
        self.env = Environment(loader=FileSystemLoader("templates"))

    def generate(self, data: dict, output_path="report.html"):
        template = self.env.get_template("report.html")
        html = template.render(
            title="Daily Automation Report",
            date=datetime.utcnow(),
            data=data
        )

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(html)

        return output_path
