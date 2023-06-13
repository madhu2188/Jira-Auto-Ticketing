import time
from jira_ticketing_version2 import check_and_create_issue
from slack_notification import send_slack_notification

def main(req_dict):
    try:
        
        channel_name = req_dict['channels'].capitalize()  # Replace with the actual channel name
        summary = req_dict['summary']  # Replace with the actual summary
        start_time = time.monotonic()
        final_value = check_and_create_issue(summary, channel_name)
        time_taken = time.monotonic() - start_time
        print(f"Time Taken: {time_taken}")
        # print(final_value)
        

    except Exception as e:
        print(f"Error processing data: {e}")

    send_slack_notification(final_value, channel_name,summary)

