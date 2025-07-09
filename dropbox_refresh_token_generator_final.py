import requests
import webbrowser

# 🔐 Pre-fill your app credentials here
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
print("If it doesn't open, copy this URL into your browser manually:")
print(auth_url)
webbrowser.open(auth_url)

# Step 2: Prompt user for code
auth_code = input("\n📥 Paste the code you received from the URL: ").strip()

# Step 3: Exchange code for refresh token
print("\n🔄 Exchanging code for refresh token...")
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

# Step 4: Print result
if response.status_code == 200:
    data = response.json()
    print("\n✅ Success! Save these values:")
    print(f"REFRESH_TOKEN = {data.get('refresh_token', '❌ Not returned')}")
    print(f"ACCESS_TOKEN = {data.get('access_token', '❌ Not returned')}")
    print(f"EXPIRES_IN = {data.get('expires_in', 'N/A')} seconds")
    print(f"SCOPES = {data.get('scope', 'N/A')}")
else:
    print("\n❌ Failed to exchange token:")
    print(response.text)
