from flask import Flask, jsonify
import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Hello from Flask</h1>'

@app.route('/health')
def health():
    return jsonify({"status": "healthy", "timestamp": str(datetime.datetime.now())})

@app.route('/version')
def version():
    return jsonify({"version": "1.0.0-staging", "environment": "staging"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)