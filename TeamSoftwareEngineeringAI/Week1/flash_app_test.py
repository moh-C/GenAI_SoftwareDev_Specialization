import requests
import json
import pytest

def test_server_connection():
    """Test if server is running and accessible"""
    try:
        response = requests.get("http://127.0.0.1:5000/api/greet/test")
        assert response.status_code == 200, "Server is not running or not accessible"
    except requests.ConnectionError:
        pytest.fail("Failed to connect to server")

def test_get_greeting():
    """Test GET request with name parameter"""
    test_name = "test_user"
    
    try:
        response = requests.get(f"http://127.0.0.1:5000/api/greet/{test_name}")
        assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
        
        response_data = response.json()
        assert isinstance(response_data, dict), "Response is not a valid JSON object"
        assert "message" in response_data, "Response missing required 'message' field"
        assert response_data["message"] == f"Hello, {test_name}!", f"Expected message 'Hello, {test_name}!', got '{response_data.get('message')}'"
        
    except requests.ConnectionError:
        pytest.fail("Failed to connect to server")
    except json.JSONDecodeError:
        pytest.fail("Server response is not valid JSON")
    except Exception as e:
        pytest.fail(f"Unexpected error: {str(e)}")

def test_invalid_request():
    """Test handling of invalid URL"""
    try:
        response = requests.get("http://127.0.0.1:5000/api/greet/")
        assert response.status_code == 404, "Server should return 404 for invalid URL"
    except requests.ConnectionError:
        pytest.fail("Failed to connect to server")

if __name__ == "__main__":
    print("Running Flask app tests...")
    try:
        test_server_connection()
        test_get_greeting()
        test_invalid_request()
        print("All tests passed successfully!")
    except Exception as e:
        print(f"Tests failed: {str(e)}")
