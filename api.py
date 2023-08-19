import requests

# Replace with your authorization token
u1="http://20.244.56.144/train/auth"
body={
   "companyName": "Srini railways",
    "clientID": "889ec8b3-5a51-45dd-85c7-057fb3bcf646",
    "clientSecret": "zxPbmXGYPZRoCcAj",
    "ownerName": "srinithi",
    "ownerEmail": "srinithirajsekaran@gmail.com",
    "rollNo": "CB.EN.U4CSE20362"
}
x = requests.post(u1, json=body)
AUTH_TOKEN = x.json()['access_token']
TRAIN_API_URL = "http://20.244.56.144/train/trains"

headers = {
    "Authorization": f"Bearer {AUTH_TOKEN}"
}

response = requests.get(TRAIN_API_URL, headers=headers)

if response.status_code == 200:
    train_data = response.json()
    print(train_data)
else:
    print(f"Error: {response.status_code}")


TRAIN_API_URL = "http://20.244.56.144/train/trains/2344"

headers = {
    "Authorization": f"Bearer {AUTH_TOKEN}"
}

response = requests.get(TRAIN_API_URL, headers=headers)

if response.status_code == 200:
    train_data = response.json()
    print(train_data)
else:
    print(f"Error: {response.status_code}")
