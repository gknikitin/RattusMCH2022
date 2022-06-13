import sys
import re
import os
import json

import requests
import textwrap
from bs4 import BeautifulSoup


class GrabberArticle:
   
    url = ""
    filename = ""
    path = ""
    content_tags = ['p']
    wrap = 80

    def __init__(self, url_address):
        self.url = url_address
    
        path_arr = self.url.split('/')
        if path_arr[-1] != '':
            self.filename = path_arr[-1] + ".txt"
            self.path = os.getcwd() + "/".join(path_arr[1:-1])
        else:
            self.filename = path_arr[-2] + ".txt"
            self.path = os.getcwd() + "/".join(path_arr[1:-2])
        if not os.path.exists(self.path):
            os.makedirs(self.path)

    def write_in_file(self, text):
        
        file = open(str(self.path) + '/' + str(self.filename), mode="w")
        file.write(text)
        file.close()

    def get_text(self):
       
        r = requests.get(self.url).text
        soup = BeautifulSoup(r, 'html.parser')
        content = soup.find_all(self.content_tags)
       
        wrapped_text = ""
        for p in content:
            if p.text != '':
                links = p.find_all('a')
                if links != '':
                    for link in links:
                        p.a.replace_with(link.text + str("[" + link['href'] + "]"))
                wrapped_text += ''.join(textwrap.fill(p.text, self.wrap)) + "\n\n"
        self.write_in_file(wrapped_text)


if __name__ == "__main__" and (len(sys.argv) > 1):
    try:
        mr = GrabberArticle(sys.argv[1])
        mr.get_text()
        print("Successfully processed")
    except Exception:
        print("Error processing URL")