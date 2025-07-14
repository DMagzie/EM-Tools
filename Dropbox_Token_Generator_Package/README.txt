# Dropbox Access Token Generator

This package includes a working Python script to generate a short-lived Dropbox access token using the OAuth2 authorization code flow and your Dropbox app credentials.

---

## 🔧 Files Included

- `dropbox_refresh_token_generator_final.py`: Main script to request access token and refresh token
- `.access_token`: Will be generated in your working folder when the script is run

---

## 🚀 How to Use

1. Replace the placeholders in the script:
   - `APP_KEY = "your_app_key_here"`
   - `APP_SECRET = "your_app_secret_here"`

2. Run the script:
   ```bash
   python3 dropbox_refresh_token_generator_final.py
   ```

3. Follow the instructions:
   - A browser will open with a Dropbox login/authorize screen
   - Copy the URL or use the code returned in your browser
   - Paste the code into the terminal prompt

4. The script will:
   - Retrieve your `access_token` and `refresh_token`
   - Save the `access_token` to `.access_token` for use by the uploader script
   - Print the `refresh_token` to save for reuse

---

## 🔒 Security Reminder

- Keep `.access_token` private
- Save the `refresh_token` somewhere secure for future refreshes
