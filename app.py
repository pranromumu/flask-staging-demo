# BAD VERSION - INTENTIONAL BREAK 
from flask import Flask 
import datetime 
 
app = Flask(__name__) 
 
@app.route('/') 
def home(): 
    # INTENTIONAL BUG: Divide by zero error 
    result = 10 / 0  # This will crash! 
    return "Hello" 
 
@app.route('/health') 
def health(): 
    # Health check also broken 
    return "unhealthy" 
 
if __name__ == '__main__': 
    app.run(host='0.0.0.0', port=5000) 
