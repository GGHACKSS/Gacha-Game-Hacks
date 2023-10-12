import requests

# Define the URL
url = "http://lunime.com/gachastudiobeta/studiologin.php"

# Prompt the user for account and password
accountx = input("Enter your account: ")
passx = input("Enter your password: ")

# Create the data payload
data = {
    "accountx": accountx,
    "passx": passx
}

try:
    # Send the HTTP POST request
    response = requests.post(url, data=data)

    # Check the response status code
    if response.status_code == 200:
        # Request was successful, print the response content
        print("Response Content:")
        print(response.text)
    else:
        print(f"Request failed with status code {response.status_code}")
except Exception as e:
    print(f"An error occurred: {str(e)}")
