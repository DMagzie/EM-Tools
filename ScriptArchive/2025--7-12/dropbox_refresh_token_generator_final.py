import requests

# === 🔑 Dropbox App Credentials ===
APP_KEY = "your_app_key_here"
APP_SECRET = "your_app_secret_here"
REFRESH_TOKEN = "your_refresh_token_here"

# === 💾 Output file ===
ACCESS_TOKEN_FILE = ".access_token"

# === 🔄 Request new access token ===
def get_access_token():
    url = "https://api.dropboxapi.com/oauth2/token"
    data = {
        "grant_type": "refresh_token",
        "refresh_token": REFRESH_TOKEN,
        "client_id": APP_KEY,
        "client_secret": APP_SECRET
    }
    r = requests.post(url, data=data)
    r.raise_for_status()
    return r.json()["access_token"]

if __name__ == "__main__":
    try:
        access_token = get_access_token()
        with open(ACCESS_TOKEN_FILE, "w") as f:
            f.write(access_token)
        print(f"✅ New access token saved to {ACCESS_TOKEN_FILE}")
    except Exception as e:
        print(f"❌ Failed to refresh token: {e}")
