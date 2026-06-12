import os 
from dotenv import load_dotenv 
 
# Load environment-specific .env file 
env = os.getenv('ENVIRONMENT', 'development') 
load_dotenv(f'.env.{env}') 
 
class Config: 
    SECRET_KEY = os.getenv('SECRET_KEY') 
    DATABASE_URL = os.getenv('DATABASE_URL') 
    DEBUG = os.getenv('DEBUG', 'False').lower() == 'true' 
 
    @classmethod 
    def print_config(cls): 
        print(f"Environment: {env}") 
        print(f"Debug mode: {cls.DEBUG}") 
        print(f"DB URL: {cls.DATABASE_URL[:20]}...") 
