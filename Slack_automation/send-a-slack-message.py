from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import os
from dotenv import load_dotenv

load_dotenv()

client = WebClient(token=os.getenv("SLACK_BOT_TOKEN"))
channel_id = os.getenv("SLACK_CHANNEL")  # Must be channel ID, not name

# Join channel first (if not already joined)
try:
    client.conversations_join(channel=channel_id)
except SlackApiError as e:
    if e.response["error"] != "method_not_supported_for_channel_type":
        print("Join error:", e.response["error"])

# Send message
try:
    client.chat_postMessage(channel=channel_id, text="🚀 Hello from Python!")
    print("Message sent!")
except SlackApiError as e:
    print("Post error:", e.response["error"])
