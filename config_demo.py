import os 
from dotenv import load_dotenv 
 
# Load .env file (local development only) 
load_dotenv() 
 
class Config: 
    SECRET_KEY = os.getenv('SECRET_KEY', 'default-dev-key') 
    DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///local.db') 
    API_KEY = os.getenv('API_KEY', 'test-key-123') 
    ENVIRONMENT = os.getenv('ENVIRONMENT', 'development') 
 
if __name__ == '__main__': 
    print(f"Environment: {Config.ENVIRONMENT}") 
    print(f"Secret Key: {Config.SECRET_KEY[:10]}...") 
    print(f"Database: {Config.DATABASE_URL}") 
    print(f"API Key exists: {bool(Config.API_KEY)}") 
