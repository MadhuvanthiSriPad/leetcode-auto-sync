import os
import subprocess
import requests
from datetime import datetime

# GitHub repository path 
GITHUB_REPO_PATH = '/Users/madwhoo/Desktop/projects/leetcode-auto-sync'  # Update this with your repo path

# LeetCode submission API endpoint
LEETCODE_API_URL = "https://leetcode.com/api/submissions/"

# GitHub repository name
GITHUB_REPO_NAME = "leetcode-auto-sync"

# Your GitHub username
GITHUB_USERNAME = "MadhuvanthiSriPad"  # Update with your GitHub username

# Set solutions directory
solutions_path = os.path.join(GITHUB_REPO_PATH, "solutions")
os.makedirs(solutions_path, exist_ok=True)

# Function to fetch LeetCode submissions
def fetch_leetcode_submissions():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    }
    # Add your LeetCode login cookies here
    cookies = {
        'LEETCODE_SESSION': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJfYXV0aF91c2VyX2lkIjoiNzkyNDc3MiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImFsbGF1dGguYWNjb3VudC5hdXRoX2JhY2tlbmRzLkF1dGhlbnRpY2F0aW9uQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6ImYxM2Q3YzU5YjJjYjUzMzlhNThkMjA1NzNiZTI4ODg4ZGU2YjM5ZWRiMDdhZjgwNmEwZjEwYmNkZGVmMDhmYmMiLCJzZXNzaW9uX3V1aWQiOiI0MmQ4MTU1MSIsImlkIjo3OTI0NzcyLCJlbWFpbCI6Im1hZGh1dmFudGhpLnNyaXBhZEBnbWFpbC5jb20iLCJ1c2VybmFtZSI6Im1hZGh1dmFudGhpX3MiLCJ1c2VyX3NsdWciOiJtYWRodXZhbnRoaV9zIiwiYXZhdGFyIjoiaHR0cHM6Ly9hc3NldHMubGVldGNvZGUuY29tL3VzZXJzL2F2YXRhcnMvYXZhdGFyXzE2Njc3MzQ1MDUucG5nIiwicmVmcmVzaGVkX2F0IjoxNzQxODQzMzkwLCJpcCI6IjQ1LjI1MS4zMy45NCIsImlkZW50aXR5IjoiYjk3N2UxMGQxY2IyNjEwNzkwOWU5N2Q1MWE2ODgzMjMiLCJkZXZpY2Vfd2l0aF9pcCI6WyJlMjBlNzIxMWY0MWRiZTZiMWI2Zjg2ZTVjZGFlMzViMyIsIjQ1LjI1MS4zMy45NCJdfQ.5qAcSqJuPfFozmeUicYDTlwH9uiI9B3ZhticdsKvryA'  # Replace with your actual session cookie
    }

    response = requests.get(LEETCODE_API_URL, headers=headers, cookies=cookies)
    submissions = response.json()

    # Print the response to check its structure
    print(submissions)
    
    return submissions

# Function to save solutions to GitHub repository
def save_solution_to_repo(submission):
    problem_slug = submission.get('titleSlug', submission.get('title_slug', 'default_slug'))
    
    # Use the fallback value 'default_slug' if both are missing
    if problem_slug == 'default_slug':
        print(f"Missing key 'titleSlug' in submission: {submission}")
        return
    
    try:
        problem_title = submission['title']
        solution_code = submission['code']

        # Create a file for the problem in the 'solutions' directory
        file_path = os.path.join(solutions_path, f"{problem_slug}.py")
        
        # Save the solution to the file
        with open(file_path, "w") as file:
            file.write(solution_code)
        
        print(f"Saved solution for {problem_title} to {file_path}")
    except KeyError as e:
        print(f"Missing key {e} in submission: {submission}")

# Function to commit and push changes to GitHub
def git_commit_and_push():
    # Change the working directory to the GitHub repo
    os.chdir(GITHUB_REPO_PATH)
    
    # Stage all the changes
    subprocess.run(["git", "add", "."])

    # Commit the changes
    commit_message = f"Sync solutions: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    subprocess.run(["git", "commit", "-m", commit_message])

    # Push the changes
    subprocess.run(["git", "push", "origin", "main"])

# Main function to sync solutions
def sync_solutions():
    submissions = fetch_leetcode_submissions()

    # Loop through the submissions
    for submission in submissions.get('submissions_dump', []):
        save_solution_to_repo(submission)
    
    git_commit_and_push()
    print("✅ Solutions synced to GitHub!")

if __name__ == "__main__":
    print(f"GITHUB_REPO_PATH is: {GITHUB_REPO_PATH}")
    sync_solutions()
