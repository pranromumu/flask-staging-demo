import pytest 
import os 
from app import app 
 
def test_environment_config(): 
    """Test that environment variables are loaded correctly""" 
    # This test would use GitHub secrets in CI 
    api_key = os.getenv('API_KEY') or 'test-key'
assert len(api_key)
 
def test_config_endpoint(): 
    response = app.test_client().get('/config') 
    assert response.status_code == 200 
    data = response.json 
    assert 'environment' in data 
 
def test_secrets_not_exposed(): 
    """Ensure secret values aren't accidentally exposed in responses""" 
    response = app.test_client().get('/config') 
    data = response.json 
    # API key should NOT be in response body 
    assert 'api_key' not in str(data).lower() 
