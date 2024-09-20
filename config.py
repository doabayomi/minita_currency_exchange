import os
from dotenv import load_dotenv
"""Getting environmental variables in deployment"""
load_dotenv()

class Config:
    # Get API key from environment variable
    MARKET_AUX_API_KEY = os.getenv("MARKET_AUX_API_KEY")
