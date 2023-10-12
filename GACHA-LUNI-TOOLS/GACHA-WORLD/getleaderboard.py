import requests

def download_leaderboard():
    url = "http://gachabaka.com/data/worldgetleaderboard.php"

    payload = {
        "systemCall": "1",
        "leaderCall": "1",  # Change this value based on your leaderboardpick logic
    }

    try:
        response = requests.post(url, data=payload)
        response.raise_for_status()

        # Assuming the response contains data in URL-encoded format
        leaderboard_data = response.text
        print("Leaderboard Data:")
        print(leaderboard_data)

        # You can parse and process the data here as needed.

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    download_leaderboard()
