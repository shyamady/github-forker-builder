import requests
import sys
import json
from bs4 import BeautifulSoup
import csv

GITHUB_API_URL = 'https://api.github.com'

def get_forker_list(user, repo):
  r = requests.get("https://github.com/%s/%s/network/members" % (user, repo))
  soup = BeautifulSoup(r.content, "html.parser")
  word_class = soup.find_all("a", {'data-hovercard-type': 'user'})
  word_list = [x.text.replace("\n"," ") for x in word_class]
  return word_list

def get_userinfo(username_list):
  for username in username_list:
    url = '%s/users/%s' % (GITHUB_API_URL, username[0])
    r = requests.get(url='%s' % url, headers={'Authorization': 'token %s' % token})
    r_body = json.loads(r.text)  
    bio = r_body['bio']
    if bio is not None:
        bio = bio.replace('\n', ' ')
    with open('userinfo.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow([r_body['name'], username[0], r_body['email'], r_body['location'], bio])        
  return

if __name__ == '__main__':
  if len(sys.argv) != 4:
      exit(1)

  user = sys.argv[1]
  repo = sys.argv[2]
  token = sys.argv[3]

  username_list = get_forker_list(user, repo)
  userinfo_list = get_userinfo(token, username_list)
