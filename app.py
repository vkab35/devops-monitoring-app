from flask import Flask
import psutil

app = Flask(__name__)

@app.route('/')
def home():
    cpu = psutil.cpu_percent()
    memory = psutil.virtual_memory().percent
    return f"DevOps Monitoring App<br>CPU: {cpu}%<br>Memory: {memory}%"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)