    """
ai_service.py - OpenAI Integration for AI Feedback

This file handles all communication with the OpenAI API.
It provides functions to generate personalized feedback for clients
based on their workout and nutrition data.

This version uses Python's built-in libraries (no pip install needed!)
- urllib.request: for making HTTP requests to the API
- json: for converting data to/from JSON format

Before using this file, make sure you have:
1. Created a .env file with your OpenAI API key
"""

# Import urllib.request to make HTTP requests (built into Python)
import urllib.request

# Import json to work with JSON data (built into Python)
import json

# Import os to work with file paths (built into Python)
import os


def load_api_key():
    """
    Read the OpenAI API key from the .env file.

    We read the file manually instead of using python-dotenv
    so students don't need to install any packages.

    Returns:
        The API key as a string, or None if not found
    """

    # Check if the .env file exists
    if not os.path.exists('.env'):
        print("ERROR: No .env file found!")
        print("")
        print("To fix this:")
        print("1. Run seed_database.py to create the .env template")
        print("2. Edit .env and add your OpenAI API key")
        return None

    # Open and read the .env file
    with open('.env', 'r') as file:
        # Read all lines from the file
        lines = file.readlines()

    # Look through each line for the API key
    for line in lines:
        # Skip empty lines and comments (lines starting with #)
        line = line.strip()
        if line == '' or line.startswith('#'):
            continue

        # Check if this line contains our API key
        if line.startswith('OPEN_AI_ACCESS_KEY='):
            # Extract the key (everything after the = sign)
            api_key = line.split('=', 1)[1]
            return api_key

    # Didn't find the API key
    return None


def get_api_key():
    """
    Get the OpenAI API key and validate it.

    Returns:
        The API key if valid, or None if missing/invalid
    """

    # Load the API key from the .env file
    api_key = load_api_key()

    # Check if we found a key
    if api_key is None:
        return None

    # Check if the key is still the placeholder text
    if api_key == 'your_api_key_here':
        print("ERROR: OpenAI API key not configured!")
        print("")
        print("To fix this:")
        print("1. Open the .env file in this folder")
        print("2. Replace 'your_api_key_here' with your actual OpenAI API key")
        print("3. Save the file and try again")
        print("")
        print("Get your API key from: https://platform.openai.com/api-keys")
        return None

    return api_key


def call_ai(prompt):
    """
    Send a prompt to the AI and get a response.

    Args:
        prompt: The text prompt to send to the AI

    Returns:
        The AI's response as a string, or None if there was an error
    """

    # First, get the API key
    api_key = get_api_key()

    # If we couldn't get an API key, return None
    if api_key is None:
        return None

    # Now we need to call the OpenAI API
    # We'll use urllib.request to make an HTTP POST request

    # The URL for OpenAI's chat completions API
    url = "https://api.openai.com/v1/chat/completions"

    # Create the data we'll send to the API
    # This is the format OpenAI expects
    request_data = {
        "model": "gpt-4",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    # Convert the data to JSON format (a string)
    json_data = json.dumps(request_data)

    # Convert the JSON string to bytes (required for urllib)
    data_bytes = json_data.encode('utf-8')

    # Create the HTTP request
    request = urllib.request.Request(url)

    # Add the required headers
    # Authorization: tells OpenAI who we are (using our API key)
    # Content-Type: tells the API we're sending JSON data
    request.add_header('Authorization', f'Bearer {api_key}')
    request.add_header('Content-Type', 'application/json')

    # Try to send the request and get a response
    try:
        # Send the request to OpenAI
        response = urllib.request.urlopen(request, data_bytes)

        # Read the response data
        response_data = response.read()

        # Convert the response from JSON to a Python dictionary
        result = json.loads(response_data)

        # Extract the feedback text from the response
        # The response structure is: result['choices'][0]['message']['content']
        feedback = result['choices'][0]['message']['content']

        # Return the generated feedback
        return feedback

    except urllib.error.HTTPError as error:
        # Something went wrong with the API call
        print(f"ERROR: API request failed with status {error.code}")

        # Try to read the error message
        error_body = error.read().decode('utf-8')
        print(f"Details: {error_body}")
        return None

    except Exception as error:
        # Some other error occurred
        print(f"ERROR: Could not generate feedback: {error}")
        return None
