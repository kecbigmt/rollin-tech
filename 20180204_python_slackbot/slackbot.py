import requests, json

header = {
    "Authorization":"Bearer xoxp-184717347331-189088339746-243930928130-2f2e7d9eacb6b3eaae75b3146f14f6db",
    "Content-type":"application/json"
}
data = """{"channel": "C94L04EDV","text": "otsu"}"""

r = requests.post("https://slack.com/api/chat.postMessage", headers=header, data=data)
