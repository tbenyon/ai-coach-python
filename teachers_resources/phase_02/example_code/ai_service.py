"""
AI Service
Functions to interact with OpenAI API
"""

import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def get_openai_client():
    """
    Initialize and return an OpenAI client.
    Raises an error if the API key is not found.
    """
    api_key = os.getenv('OPEN_AI_ACCESS_KEY')

    if not api_key:
        raise ValueError(
            "⚠️  WARNING: OPEN_AI_ACCESS_KEY not found in .env file!\n"
            "Please add your OpenAI API key to the .env file:\n"
            "OPEN_AI_ACCESS_KEY=your_api_key_here"
        )

    return OpenAI(api_key=api_key)

def generate_response(prompt, model="gpt-4"):
    """
    Generate a response from OpenAI API

    Args:
        prompt (str): The input prompt to send to the API
        model (str): The model to use (default: gpt-4)

    Returns:
        str: The generated response text
    """
    try:
        client = get_openai_client()

        response = client.responses.create(
            model=model,
            input=prompt
        )

        return response.output_text

    except ValueError as e:
        # Re-raise environment variable errors
        raise e
    except Exception as e:
        raise Exception(f"Error calling OpenAI API: {str(e)}")