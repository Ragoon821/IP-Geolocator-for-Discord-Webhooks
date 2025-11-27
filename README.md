# Python Geolocation Discord Webhook Script

A simple Python script that collects basic system information (IP address, hostname, user profile) and sends it to a Discord webhook along with the IP's country of origin.

## Features

- Retrieves the local machine's:
  - IP address  
  - Hostname  
  - Windows user profile path
- Gets the country of origin for the IP using a free geolocation API (`ip-api.com`)
- Sends all information to a Discord webhook as a formatted message
- Uses only **built-in Python modules** (`socket`, `os`, `urllib`, `json`)  

## Requirements

- Python 3.6+  
- A Discord webhook URL

No external libraries required.

## Usage

1. **Clone or download** this repository.
2. **Edit the script** to replace the placeholder `YOUR_WEBHOOK_URL` with your Discord webhook URL.
3. **Run the script**:

```bash
python geolocation_webhook.py
