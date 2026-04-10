import requests

API_KEY = 'MY_API_KEY'
#i have removed my api key for privacy

url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent"

headers = {
    "x-goog-api-key": API_KEY,
    'Content-Type': 'application/json'
}


def inp():
    # db = ""
    while True:
        p = input('enter prompt: ')
        if p == 'stop':
            break
        payload = {
            "contents": [
                {
                    "parts": [
                        {"text": p}
                    ]
                }
            ]
        }
        response = requests.post(url, headers=headers, json=payload)
        # print("Status: ", response.status_code)
        data = response.json()
        # print(data)
        if "candidates" in data:
            print(data["candidates"][0]["content"]["parts"][0]["text"])
        else:
            print("Error", data)
        # db += p


inp()
