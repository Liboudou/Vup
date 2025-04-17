from dotenv import load_dotenv
from __init__ import *
import os

def main():
    load_dotenv()
    api_key = os.getenv("API_KEY")
    debug = os.getenv("DEBUG")

    print(f"API_KEY: {api_key}")
    print(f"DEBUG mode: {debug}")

if __name__ == "__main__":
    main()
    print(API_KEY)
    