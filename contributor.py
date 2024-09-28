import requests
import sys

# GitHub API URL
API_URL = "https://api.github.com"

def github_api_get(endpoint):
    """Send a GET request to the GitHub API."""
    url = f"{API_URL}/{endpoint}"

    # Send a GET request to the GitHub API
    response = requests.get(url)

    # Raise an exception if the request was unsuccessful
    response.raise_for_status()  # Will raise an HTTPError for bad responses (4xx or 5xx)
    
    return response.json()

def list_contributors(repo_owner, repo_name):
    """List contributors to the specified repository."""
    endpoint = f"repos/{repo_owner}/{repo_name}/contributors"

    # Fetch the list of contributors on the repository
    try:
        contributors = github_api_get(endpoint)
        contributor_usernames = [user['login'] for user in contributors]
        
        # Display the list of contributors
        if not contributor_usernames:
            print(f"No contributors found for {repo_owner}/{repo_name}.")
        else:
            print(f"Contributors to {repo_owner}/{repo_name}:")
            print("\n".join(contributor_usernames))

    except requests.exceptions.HTTPError as e:
        print(f"Error fetching data: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script_name.py <repo_owner> <repo_name>")
        sys.exit(1)

    repo_owner = sys.argv[1]
    repo_name = sys.argv[2]

    print(f"Listing contributors to {repo_owner}/{repo_name}...")
    list_contributors(repo_owner, repo_name)
