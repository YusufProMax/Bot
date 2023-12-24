import requests


def login_def(login, password):
    url = "https://api.marsit.uz/api/v1/auth/signin"

    payload = {
        "student": {
            "external_id": login,
            "code": f"{password}",
            "role": "student"
        }
    }

    response = requests.post(url, json=payload)
    if response.status_code == 200:
        data = response.json()
        return data.get('user')
    else:
        return False