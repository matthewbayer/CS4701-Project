import time
from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
from requests_html import HTMLSession
import userdata


# session = requests.Session()
# s = session.post("https://piazza.com/class", data=userdata.data, cookies=userdata.cookies)

# url = "https://piazza.com/class/kea8ntdsn097ev?cid=1494"
# s = session.get(url)
# soup = BeautifulSoup(s.content, "html.parser")
# print(soup.get_text())


session = HTMLSession()

r = session.get("https://piazza.com/")
r = session.post("https://piazza.com/class", data=userdata.data)
page = session.get("https://piazza.com/class/kea8ntdsn097ev?cid=1")
page.html.render()
soup = BeautifulSoup(page.html, "html.parser")
print(soup.get_text())

# data = '{"method":"content.get","params":{"cid":"khksgq944s2172","nid":"kek9zeb4r1g3ir","student_view":false}}'
# r = session.post('https://piazza.com/logic/api', data=userdata.data)
# soup = BeautifulSoup(r.html, "html.parser")
# print(soup.get_text())


# r = session.get("https://piazza.com/class/kea8ntdsn097ev?cid=1494")

# soup = BeautifulSoup(r.html.text, "html.parser")

# url = "https://piazza.com/class/kea8ntdsn097ev?cid=1"
# page = urlopen(url)
# html = page.read().decode("utf-8")
# soup = BeautifulSoup(html, "html.parser")

# print(soup.get_text())
