from slack import WebClient
from slack.errors import SlackApiError
import time
from markdown_formatter import format_slack_message
import config_file

def send_slack_notification(final_value, slack_channel,summary):
    # Initialize the Slack API client
    slack_client = WebClient(config_file.SLACK_TOKEN)
    channel_name = slack_channel # Replace with the logic to extract the channel name

    try:
        message_text = format_slack_message(final_value,summary)
        response = slack_client.chat_postMessage(
            channel=f"#{channel_name.lower()}-monitoring-triage",
            text=message_text
        )
        print("Notification sent: %s" % response["ts"])
        time.sleep(1)  # Add a 1 second delay between API requests

        # Delete the row from the collection or perform other necessary actions

    except SlackApiError as e:
        print("Error sending notification: %s" % e)



