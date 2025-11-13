from flask import Flask, request, jsonify, render_template_string
from pprint import pprint

app = Flask(__name__)

alerts = []

# HTML page for viewing alerts
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Alert Viewer</title>
    <style>
        body { font-family: Arial; margin: 20px; }
        table { border-collapse: collapse; width: 100%; }
        th, td { border: 1px solid #ddd; padding: 8px; }
        th { background-color: #007ACC; color: white; }
    </style>
</head>
<body>
    <h2>Received Alerts</h2>
    <table>
        <tr>
            <th>#</th>
            <th>Alert Payload</th>
        </tr>
        {% for idx, alert in enumerate(alerts) %}
        <tr>
            <td>{{ idx + 1 }}</td>
            <td><pre>{{ alert | tojson(indent=2) }}</pre></td>
        </tr>
        {% endfor %}
    </table>
</body>
</html>
"""

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    alerts.append(data)
    print("Received alert:")
    pprint(data)  # pretty print to terminal
    return jsonify({"status": "received"}), 200

@app.route('/alerts', methods=['GET'])
def get_alerts():
    return render_template_string(HTML_TEMPLATE, alerts=alerts)

@app.route('/', methods=['GET'])
def home():
    return "<h2>Alert Viewer is running. Go to <a href='/alerts'>/alerts</a> to view alerts.</h2>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
