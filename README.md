# Brute-Force-Login-Script
A web login brute force script made through the Python 101 for Ethical Hacking course at TCM Academy. 

*LEGAL DISCLAIMER:*
- Use this script only on systems you own or have explicit permission to test.
Unauthorized brute‑forcing is illegal and unethical. This repository is for educational and lab‑use only.

*Note:*
- This repo does not include any password wordlists. You must supply your own top-100.txt or custom list.

This is a simple web login brute‑force script I built while going through the Python 101 course on TCM Academy. The goal of this project was to understand how brute forcing works at a basic level such as sending repeated requests, checking server responses, and automating login attempts. 

I decided to test the script on the DVWA(Damn Vulnerable Web Application) brute force module which is intentionally designed for training and legal practice.

*What this script does:*
- Cycles through a list of usernames
- Reads passwords from the provided wordlist.(top-100.txt)
- Sends login attempts to DVWA
- Detects a succesful login based on text returned by the page.
- Displays progress in real time
- Then finally, stops as soon as it finds the valid password.

*Why my script has some differences from the original TCM Academy script:*
- Although the script is based on the original TCM course structure I had to make a few adjustments so it would work correctly with DVWA such as:
- Changing the target URL, The original course uses a raw IP and port example. Since DVWA doesn't run on port 3306 I had to change it to the actual URL I was testing
- DVWA requires a valid "PHPSESSID" and a security level cookie, without those DVWA would not accept any login attempts at all. Which is why I added:
  " cookies = {
    "PHPSESSID": "your-session-id",
    "security": "low"
   } " This mimics an authenticated DVWA session.
- I also removed ".decode()" since passwords were no longer encoded. The original script encoded passwords into bytes, but DVWA accepts normal strings without encoding. That caused errors, so I kept everything in string format to match DVWA’s behavior.
- I tried to keep the script as close to the original as possible. Aside from the necessary changes I needed for the script to run properly when testing on DVWA I kept the looping structure, print format, early-exit structure "(sys.exit())", and the needle response check. This perserves the original workflow from the Python 101 course while working against a real web app.

*Some things I learned while encountering difficulties when doing the project through this course:*
- The original course example used POST requests, but DVWA’s brute force module relies on GET parameters. Automation only works if the script matches the target exactly.
Seeing GET/POST differences in action deepened my understanding of HTTP fundamentals.
- ".decode()" errors would crash the script. The original code in the course used ".decode()" which gave me "AttributeError: 'str' object has no attribute 'decode'"
The reason for this error is because Python 3 strings are already in unicode, they don't need decoding. The fix for this was removing all ".decode()" calls and keeping everything as clean strings. This helped me understand Python 2 and Python 3 encoding differences, when to use ".encode()" and ".decode()", and also why handling bytes properly matter when writing scripts in cybersecurity. 

*How this script works:*
- First you need a web application you are authorized to test.(I used DVWA)
- Make sure you have mariadb and the apache2 web server running.
- Log into DVWA normally then proceed to the brute force module page.
- Copy your PHPSESSID from your browser using developer tools then input it into your script, Make sure your DVWA security is set to low.
- In your terminal run "python3 web-brute.py" or whatever name you set for your script.
- Once running the script you should see attempts scrolling line by line until it reaches the correct password. 
