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
        'LEETCODE_SESSION': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhY2NvdW50X3ZlcmlmaWVkX2VtYWlsIjpudWxsLCJhY2NvdW50X3VzZXIiOiI5d2tuOCIsIl9hdXRoX3VzZXJfaWQiOiIxNjYzNjI5MiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImFsbGF1dGguYWNjb3VudC5hdXRoX2JhY2tlbmRzLkF1dGhlbnRpY2F0aW9uQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6ImMxMzA1NmY3ZjNkMGJmNmEzNzg0NjNkOWI0ZjM5MzUwYjJmODg0ZGI5ODg0NGNiMzhlZDFhMmQ4ZjFhNTIzNjYiLCJzZXNzaW9uX3V1aWQiOiIzMmMyYzc3MCIsImlkIjoxNjYzNjI5MiwiZW1haWwiOiJtYWRodXZhbnRoaXNyaXBhZEBnbWFpbC5jb20iLCJ1c2VybmFtZSI6Im1hZGh1dmFudGhpc3JpcGFkIiwidXNlcl9zbHVnIjoibWFkaHV2YW50aGlzcmlwYWQiLCJhdmF0YXIiOiJodHRwczovL2Fzc2V0cy5sZWV0Y29kZS5jb20vdXNlcnMvZGVmYXVsdF9hdmF0YXIuanBnIiwicmVmcmVzaGVkX2F0IjoxNzM5MzQ1NzgzLCJpcCI6IjQ1LjI1MS4zMy45NCIsImlkZW50aXR5IjoiOTlhOGI0NjE2YWYzYjM5NjM3YjM1YzMwYmNhNmY1YzQiLCJkZXZpY2Vfd2l0aF9pcCI6WyIwOTMzODFhNzdjMTQxYWVjZTMwMGY2ZTQyYjE1N2Q1YiIsIjQ1LjI1MS4zMy45NCJdfQ.xg7Fz6Kktd95gbbKG0SwZ6GdEJzbao_WwoHtBg1Aguw'  # Replace with your actual session cookie
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
