!/usr/bin/python3
"""Getting environmental variables in deployment"""
import os

class Config:
    MARKET_AUX_API_KEY = os.getenv("MARKET_AUX_API_KEY")
