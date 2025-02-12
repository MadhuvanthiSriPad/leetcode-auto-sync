import os
import requests
import json
from bs4 import BeautifulSoup
from git import Repo

# CONFIGURATION
import os

# Automatically detect the correct repo path
GITHUB_REPO_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

print("Updated GITHUB_REPO_PATH is:", GITHUB_REPO_PATH)
GITHUB_COMMIT_MESSAGE = "Auto-sync: Updated LeetCode solutions"
print("GITHUB_REPO_PATH is:", GITHUB_REPO_PATH)

# Start a session
session = requests.Session()

# Manually set session cookies (get these from your browser)
session.cookies.set("LEETCODE_SESSION", "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhY2NvdW50X3ZlcmlmaWVkX2VtYWlsIjpudWxsLCJhY2NvdW50X3VzZXIiOiI5d2tuOCIsIl9hdXRoX3VzZXJfaWQiOiIxNjYzNjI5MiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImFsbGF1dGguYWNjb3VudC5hdXRoX2JhY2tlbmRzLkF1dGhlbnRpY2F0aW9uQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6ImMxMzA1NmY3ZjNkMGJmNmEzNzg0NjNkOWI0ZjM5MzUwYjJmODg0ZGI5ODg0NGNiMzhlZDFhMmQ4ZjFhNTIzNjYiLCJzZXNzaW9uX3V1aWQiOiIzMmMyYzc3MCIsImlkIjoxNjYzNjI5MiwiZW1haWwiOiJtYWRodXZhbnRoaXNyaXBhZEBnbWFpbC5jb20iLCJ1c2VybmFtZSI6Im1hZGh1dmFudGhpc3JpcGFkIiwidXNlcl9zbHVnIjoibWFkaHV2YW50aGlzcmlwYWQiLCJhdmF0YXIiOiJodHRwczovL2Fzc2V0cy5sZWV0Y29kZS5jb20vdXNlcnMvZGVmYXVsdF9hdmF0YXIuanBnIiwicmVmcmVzaGVkX2F0IjoxNzM5MzQ1NzgzLCJpcCI6IjQ1LjI1MS4zMy45NCIsImlkZW50aXR5IjoiOTlhOGI0NjE2YWYzYjM5NjM3YjM1YzMwYmNhNmY1YzQiLCJkZXZpY2Vfd2l0aF9pcCI6WyIwOTMzODFhNzdjMTQxYWVjZTMwMGY2ZTQyYjE1N2Q1YiIsIjQ1LjI1MS4zMy45NCJdfQ.xg7Fz6Kktd95gbbKG0SwZ6GdEJzbao_WwoHtBg1Aguw")

# Fetch the submissions page
response = session.get("https://leetcode.com/submissions/")
soup = BeautifulSoup(response.text, "html.parser")

# Extract accepted submissions
submissions = []
for row in soup.find_all("tr"):
    columns = row.find_all("td")
    if len(columns) > 3:
        problem_name = columns[1].text.strip()
        status = columns[2].text.strip()
        if status == "Accepted":
            submissions.append(problem_name)

# Save solutions locally
solutions_path = os.path.join(GITHUB_REPO_PATH, "solutions")
os.makedirs(solutions_path, exist_ok=True)

for problem in submissions:
    file_path = os.path.join(solutions_path, f"{problem}.txt")
    with open(file_path, "w") as f:
        f.write(f"Solution for {problem}")

# Commit and push to GitHub
repo = Repo(GITHUB_REPO_PATH)
repo.git.add(A=True)
repo.index.commit(GITHUB_COMMIT_MESSAGE)
origin = repo.remote(name="origin")
origin.push()

print("✅ Solutions synced to GitHub!")



