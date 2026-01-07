"""
LLM initialization using Google Gemini via google-genai.
"""
import os
from google import genai
from dotenv import load_dotenv

load_dotenv()


def create_gemini_chat(model: str = "gemini-flash-latest"):
    """
    Initialize Gemini Chat client.
    Args:
        model: Gemini model name (default: gemini-1.5-flash)
        
    Returns:
        Tuple of (Gemini client, model name)
    """
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("GOOGLE_API_KEY not found in environment variables. Please set it in your .env file.")
    
    client = genai.Client(api_key=api_key)
    return client, model
