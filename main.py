import requests
import sys
from bs4 import BeautifulSoup
import csv

def get_forker_list(user, repo):
  r = requests.get("https://github.com/%s/%s/network/members" % (user, repo))
  soup = BeautifulSoup(r.content, "html.parser")
  word_class = soup.find_all("a", {'data-hovercard-type': 'user'})
  word_list = [x.text.replace("\n"," ") for x in word_class]
  return word_list

def get_userinfo(username_list):
  userinfo_list = []
  for i, username in enumerate(username_list):
    r = requests.get("https://github.com/%s" % (username))
    soup = BeautifulSoup(r.content, "html.parser")
    name = soup.find("span", "p-name")
    email = soup.find("a", "u-email")
    bio = soup.find("div", "p-note4")
    userinfo_list.append({name, username, email, bio})

if __name__ == '__main__':
  if len(sys.argv) != 3:
      exit(1)

  user = sys.argv[1]
  repo = sys.argv[2]

  username_list = get_forker_list(user, repo)
  userinfo_list = get_userinfo(username_list)
