import os
from dotenv import load_dotenv

load_dotenv()

print(os.getenv("SLACK_BOT_TOKEN"))
print("token")
print(os.getenv("SLACK_CHANNEL", "#reports"))
class Settings:
    SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
    SLACK_CHANNEL = os.getenv("SLACK_CHANNEL", "#reports")
    REPORT_TITLE = "Automated HTML Report"

settings = Settings()
