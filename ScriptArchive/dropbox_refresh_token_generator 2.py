import webbrowser
import requests

# 🔐 Paste your app credentials below
APP_KEY = "ywb1x3c744ot17c"
APP_SECRET = "1wzcm1xituufgox"
REDIRECT_URI = "http://localhost/finish"

# Step 1: Launch the authorization URL in browser
auth_url = (
    f"https://www.dropbox.com/oauth2/authorize"
    f"?client_id={APP_KEY}"
    f"&response_type=code"
    f"&token_access_type=offline"
    f"&redirect_uri={REDIRECT_URI}"
    f"&force_reapprove=true"
)

print("🔗 Opening browser for Dropbox authorization...")
print("If it doesn't open, copy this URL into your browser:")
print(auth_url)
webbrowser.open(auth_url)

# Step 2: Prompt user for code
auth_code = input("\n📥 Paste the code you received here: ").strip()

# Step 3: Exchange code for refresh token
print("\n🔄 Exchanging code for token...")
headers = {"Content-Type": "application/x-www-form-urlencoded"}
response = requests.post(
    "https://api.dropboxapi.com/oauth2/token",
    headers=headers,
    data={
        "code": auth_code,
        "grant_type": "authorization_code",
        "client_id": APP_KEY,
        "client_secret": APP_SECRET,
        "redirect_uri": REDIRECT_URI
    }
)

if response.status_code == 200:
    data = response.json()
    print("\n✅ Success! Here are your credentials:")
    print(f"REFRESH_TOKEN = {data['refresh_token']}")
    print(f"ACCESS_TOKEN = {data['access_token']}")
    print(f"EXPIRES_IN = {data['expires_in']} seconds")
    print(f"SCOPES = {data.get('scope', 'N/A')}")
    print("\n⚠️ Save your REFRESH_TOKEN for use in your scripts.")
else:
    print("\n❌ Failed to exchange token:")
    print(response.text)

