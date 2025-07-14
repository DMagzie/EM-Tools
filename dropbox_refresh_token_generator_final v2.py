import requests
import webbrowser

# === 🔐 Dropbox App Credentials ===
APP_KEY = "ywb1x3c744ot17c"
APP_SECRET = "1wzcm1xituufgox"
REDIRECT_URI = "http://localhost/finish"
ACCESS_TOKEN_FILE = ".access_token"

# === 🌐 Step 1: Open browser for OAuth2 flow ===
authorize_url = (
    "https://www.dropbox.com/oauth2/authorize"
    f"?client_id={APP_KEY}"
    f"&response_type=code"
    f"&token_access_type=offline"
    f"&redirect_uri={REDIRECT_URI}"
    f"&force_reapprove=true"
)

print("🔗 Opening browser for Dropbox authorization...")
print("If it doesn't open, copy this URL into your browser manually:")
print(authorize_url)
webbrowser.open(authorize_url)

# === 🖊 Step 2: User pastes code ===
code = input("\n📥 Paste the code you received from the URL: ").strip()

# === 🔄 Step 3: Exchange code for tokens ===
token_url = "https://api.dropboxapi.com/oauth2/token"
data = {
    "code": code,
    "grant_type": "authorization_code",
    "client_id": APP_KEY,
    "client_secret": APP_SECRET,
    "redirect_uri": REDIRECT_URI
}

try:
    response = requests.post(token_url, data=data)
    response.raise_for_status()
    token_data = response.json()

    access_token = token_data["access_token"]
    refresh_token = token_data.get("refresh_token")

    # Save short-lived access token for upload script
    with open(ACCESS_TOKEN_FILE, "w") as f:
        f.write(access_token)
    print(f"✅ Access token saved to {ACCESS_TOKEN_FILE}")

    # Print full token info for record-keeping
    print("\n✅ Success! Save these values:")
    print(f"REFRESH_TOKEN = {refresh_token}")
    print(f"ACCESS_TOKEN = {access_token}")
    print(f"EXPIRES_IN = {token_data.get('expires_in')} seconds")
    print(f"SCOPES = {token_data.get('scope')}")
except Exception as e:
    print(f"❌ Token exchange failed: {e}")
