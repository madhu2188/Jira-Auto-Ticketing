from flask import Flask, request, render_template
import main

app = Flask(__name__, template_folder='templates')

@app.route("/")
def hello():
    return render_template("index.html")

@app.route('/webhook', methods=['POST'])
def webhook():
    # Get the data from the webhook request
    data = request.get_json()
    req_dict = {}

    if 'summary' in data:
        req_dict['summary'] = data['summary']

    if 'channels' in data:
        channels = data['channels']
        prefix = '_slack-peloton_enterprise_operations_support-'
        if channels.startswith(prefix):
            remaining = channels[len(prefix):]
            req_dict['channels'] = remaining.split('-')[0]
        else:
            req_dict['channels'] = data['channels']

    if 'priority' in data:
        req_dict['priority'] = data['priority']

    # Process the webhook data
    main.main(req_dict)

    return f'Webhook received and data processed.'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
