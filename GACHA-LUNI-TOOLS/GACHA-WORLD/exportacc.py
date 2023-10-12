import requests

# Define the URL
url = "http://lunime.com/worldgachadata/registerworldreplacex.php"

# Prompt the user for input
accountx = input("Enter account value: ")
passx = input("Enter password: ")
namex = input("Enter name: ")

# Define the data to be sent in the request
data = {
    "accountx": accountx,
    "passx": passx,
    "namex": namex,
    # Add other data parameters as needed
}

try:
    # Send the POST request
    response = requests.post(url, data=data)

    # Check the response status code
    if response.status_code == 200:
        # Request was successful
        print("Request successful.")
    else:
        print(f"Request failed with status code: {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
