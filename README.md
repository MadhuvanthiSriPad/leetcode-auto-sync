# LeetCode Auto Sync

This project allows you to automatically sync your LeetCode solutions to a GitHub repository. It fetches your accepted submissions from LeetCode and saves them in your repository as Python files, categorized by problem title.

## Features
- Fetches your LeetCode submissions using the LeetCode API.
- Saves your LeetCode solutions as `.py` files in a `solutions/` directory.
- Automatically commits and pushes these solutions to your GitHub repository.
- Organizes your solutions by problem name and ensures each solution is saved in a separate file.

## Prerequisites
Before you begin, make sure you have the following installed:

1. **Python 3.x**: The script is written in Python 3. Ensure you have Python 3.x installed on your machine.
   
   You can check if you have Python 3 installed by running:
   ```bash
   python3 --version
