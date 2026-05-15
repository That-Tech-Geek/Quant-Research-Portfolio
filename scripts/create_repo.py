import os
import json
import requests

def create_github_repo():
    token = os.getenv("GITHUB_AGENT_PAT")
    if not token:
        print("GITHUB_AGENT_PAT not found")
        return None
        
    url = "https://api.github.com/user/repos"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json",
        "Content-Type": "application/json"
    }
    payload = {
        "name": "Industrialized-Quant-Research-Library",
        "description": "Industrialized Quantitative Research Library: 15 publication-ready papers (1000+ lines of LaTeX each) for Tier 1 Trading Interviews.",
        "private": False,
        "auto_init": False
    }
    
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 201:
        data = response.json()
        print(f"Successfully created repository: {data['html_url']}")
        return data['clone_url']
    else:
        print(f"Failed to create repository: {response.status_code}")
        print(response.text)
        return None

if __name__ == "__main__":
    create_github_repo()
