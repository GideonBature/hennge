import base64
import hashlib
import hmac
import time
import requests
import json
import pyotp

# Configuration
email = "infoaboutgideon@gmail.com"
shared_secret = email + "HENNGECHALLENGE003"
github_url = "https://gist.github.com/GideonBature/5e9ee752cd6573a50dcf0468dbaa506b"
solution_language = "python"
url = "https://api.challenge.hennge.com/challenges/003"

# Generate TOTP
# Step size 30 seconds, HMAC-SHA-512
time_step = 30
T0 = 0
current_time = int(time.time())
time_counter = (current_time - T0) // time_step
key = shared_secret.encode()

# Convert time_counter to bytes
time_counter_bytes = time_counter.to_bytes(8, 'big')

# HMAC-SHA-512 computation
hmac_sha512 = hmac.new(key, time_counter_bytes, hashlib.sha512).digest()

# Extract dynamic binary code from the HMAC
offset = hmac_sha512[-1] & 0x0F
code = ((hmac_sha512[offset] & 0x7F) << 24 |
        (hmac_sha512[offset + 1] & 0xFF) << 16 |
        (hmac_sha512[offset + 2] & 0xFF) << 8 |
        (hmac_sha512[offset + 3] & 0xFF))

# Generate a 10-digit TOTP password
otp = code % (10 ** 10)
otp_str = str(otp).zfill(10)

# Prepare Basic Auth header
auth_value = f"{email}:{otp_str}"
auth_header = base64.b64encode(auth_value.encode()).decode()

# Prepare JSON payload
payload = {
    "github_url": github_url,
    "contact_email": email,
    "solution_language": solution_language
}

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Basic {auth_header}"
}

# Make the POST request
response = requests.post(url, headers=headers, data=json.dumps(payload))

# Print the response
print(response.status_code)
print(response.json())
