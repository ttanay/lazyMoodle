import re
import requests
from bs4 import BeautifulSoup

class LazyMoodle:
    login_url = "http://moodle.msit.in/login/index.php"
    feedback_url = "http://moodle.msit.in/mod/feedback/complete.php?id={}&courseid&gopage=0"

    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:56.0) Gecko/20100101 Firefox/56.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate",
        "Content-Type": "application/x-www-form-urlencoded",
    }

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        data = {
            "username": self.username,
            "password": self.password,
        }
        r = requests.post(self.login_url, headers=self.headers, data=data)

        sesskey_regex = re.compile(r'"sesskey":"\w*"')
        sesskey = sesskey_regex.search(r.text)
        soup = BeautifulSoup(r.text)

