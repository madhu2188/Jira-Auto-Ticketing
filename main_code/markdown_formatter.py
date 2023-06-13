def format_slack_message(data,summary):
    """
    Formats a dictionary of data as a Markdown-formatted Slack message.

    :param data: A dictionary containing data to include in the message.
    :return: A string containing the formatted message text.
    """
    message_text = "\n\n"
    Alert = summary
    message_text += f"*{summary}:*\n```\n{data}\n```\n"
    return message_text
