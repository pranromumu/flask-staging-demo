from flask import Flask, jsonify
import datetime
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "CI/CD Deployment Demo - Running!"

@app.route('/health')
def health():
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.datetime.now().isoformat()
    })

@app.route('/version')
def version():
    return jsonify({
        'version': '1.0.0',
        'environment': os.getenv('ENVIRONMENT', 'development')
    })

@app.route('/config')
def config():
    return jsonify({
        'environment': os.getenv('ENVIRONMENT', 'development'),
        'timestamp': datetime.datetime.now().isoformat()
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)