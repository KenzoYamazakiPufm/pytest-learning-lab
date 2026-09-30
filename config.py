import os

def get_token():
    return os.getenv("API_KEY", "")

def build_header():
    return {"Authorization": f"Bearer {get_token()}"}