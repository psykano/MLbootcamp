from flask import Flask, render_template, request
import threading
import matplotlib.pyplot as plt
import io
import os
import base64

os.environ["FLASK_DEBUG"] = "development"

app = Flask(__name__)
port = 5000

# Open a ngrok tunnel to the HTTP server
public_url = ngrok.connect(port).public_url
print(" * ngrok tunnel \"{}\" -> \"http://127.0.0.1:{}\"".format(public_url, port))

# Update any base URLs to use the public ngrok URL
app.config["BASE_URL"] = public_url

def generate_bar_chart(categories, values):
  # Generate the figure
  fig = Figure()
  plot = fig.subplots()
  x = categories.split(",")
  y = values.split(",")
  plot.bar(x, y)
  plot.set_xlabel('Categories')
  plot.set_ylabel('Values')
  plot.set_title('Data Visualization')

  # Save it to a buffer
  buf = io.BytesIO()
  fig.savefig(buf, format="png")

  # Encode as base64
  data = base64.b64encode(buf.getbuffer()).decode("ascii")
  return data

@app.route('/', methods=['GET', 'POST'])
def index():
  chart_url = None

  if request.method == 'POST':
    categories = request.form['categories']
    values = request.form['values']
    chart = generate_bar_chart(categories, values)
    chart_url = chart

  return render_template('index.html', chart_url=chart_url)

if __name__ == '__main__':
    # Start the Flask server in a new thread
  threading.Thread(target=app.run, kwargs={"use_reloader": False}).start()