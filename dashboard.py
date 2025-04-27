from flask import Flask, render_template_string

app = Flask(__name__)

#to hold all the events to display
event_log = []


@app.route('/')
def home():

    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>SSPM + ITDR Security Monitor Dashboard</title>
        <meta http-equiv="refresh" content="5">  <!-- Refresh every 5 seconds -->
    </head>
    <body>
        <h1>SSPM + ITDR Security Monitor Dashboard</h1>
        <h2>Live Event Log</h2>
        <ul>
        {% for event in events %}
            <li>{{ event }}</li>
        {% endfor %}
        </ul>
    </body>
    </html>
    """

    return render_template_string(html, events=event_log)

def add_event(event_text):
    event_log.append(event_text)
    if len(event_log) > 100:
        event_log.pop(0)        #keeping the log size reasonable

def run_dashboard():
    app.run(port=5050)
