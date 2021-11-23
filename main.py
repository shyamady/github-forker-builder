import requests
import sys
from bs4 import BeautifulSoup

def get_forker_list(user, repo):
  r = requests.get("https://askvid.co")
  soup = BeautifulSoup(r.content, "html.parser")
  word_class = soup.find_all("div")
  word_list = [x.text.replace("\n"," ") for x in word_class]
  return word_list

if __name__ == '__main__':
  if len(sys.argv) != 3:
      exit(1)

  user = sys.argv[1]
  repo = sys.argv[2]

  username_list = get_forker_list(user, repo)