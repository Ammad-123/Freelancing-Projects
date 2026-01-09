from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from app.config import settings

class SlackService:
    def __init__(self):
        self.client = WebClient(token=settings.SLACK_BOT_TOKEN)

    def send_message(self, text):
        try:
            self.client.chat_postMessage(
                channel=settings.SLACK_CHANNEL,
                text=text
            )
        except SlackApiError as e:
            raise RuntimeError(e.response["error"])

    def upload_html(self, file_path):
        try:
            self.client.files_upload_v2(
                channel=settings.SLACK_CHANNEL,
                file=file_path,
                title="HTML Report"
            )
        except SlackApiError as e:
            raise RuntimeError(e.response["error"])
