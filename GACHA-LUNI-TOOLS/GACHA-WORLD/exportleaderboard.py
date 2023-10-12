import requests

def upload_code():
    url = "http://gachabaka.com/data/worldsubmitleaderboard.php"
    leaderboard_data = input("Enter your GW account strings: ")

    params = {"leaderboardata": leaderboard_data}  # Correctly construct the params dictionary

    try:
        response = requests.get(url, params=params)

        if response.status_code == 200:
            handle_complete(response.text)
        else:
            handle_io_error(response.status_code)

    except requests.exceptions.RequestException as e:
        handle_io_error(str(e))

def handle_complete(response_data):
    print("Request successful. Response data:", response_data)

def handle_io_error(error_message):
    print("IO Error:", error_message)

upload_code()
