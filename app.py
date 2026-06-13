import os 
from flask import Flask, jsonify 
import datetime 
 
# Load environment variables 
from dotenv import load_dotenv 
load_dotenv() 
 
app = Flask(__name__) 
 
# Configuration from environment 
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-key') 
app.config['ENVIRONMENT'] = os.getenv('ENVIRONMENT', 'development') 
app.config['API_BASE_URL'] = os.getenv('API_BASE_URL', 'https://api.example.com') 
 
@app.route('/') 
def home(): 
    return f''' 
 
@app.route('/config') 
def show_config(): 
    return jsonify({ 
        "environment": app.config['ENVIRONMENT'], 
        "api_configured": bool(app.config['API_BASE_URL']), 
        "secret_configured": bool(app.config['SECRET_KEY']) 
    }) 
 
if __name__ == '__main__': 
    app.run(host='0.0.0.0', port=5000) 
