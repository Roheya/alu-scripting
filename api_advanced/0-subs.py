
#!/usr/bin/python3
"""Query the Reddit API."""

import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers for a subreddit."""

    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    headers = {
    "User-Agent": "linux:alu.reddit.api.project:v1.0 (by /u/your_reddit_username)"
}
    response = requests.get(
        url,
        headers=headers,
        allow_redirects=False
    )

    if response.status_code != 200:
        return 0

    data = response.json().get("data", {})
    return data.get("subscribers", 0)

