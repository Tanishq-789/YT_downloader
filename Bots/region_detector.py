import requests

def detect_region():
    try:
        response = requests.get('https://ipinfo.io')
        data = response.json()
        return data.get('country', 'US')  # Default to US if region detection fails
    except Exception:
        return 'US'  # Default to US if there's an error