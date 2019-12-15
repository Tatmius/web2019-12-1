from django.db import models
from beautifulsoup4 import BeautifulSoup
import random
from urllib.request import urlopen
import csv
import re

# Create your models here.

def csvRead(path, num):
    with open(path, 'r',encoding="utf-8") as f:
        reader = csv.reader(f)
        line_num = 0
        while True:
            if line_num == num:
                return next(reader)
            f.readline()
            line_num += 1
    return None

def random_scrape():
    randInt=random.randint(2,16772)
    url=csvRead('Book1.csv', randInt)
    r=urlopen(url[0])
    soup = BeautifulSoup(r,"lxml",from_encoding="shift_jis")
    r.close()
    return soup

def getMainText(soup):
    main_text=(soup.find("div","main_text")).text
    endtag=re.compile("\n")
    end_tags=endtag.findall(main_text)

    for end_tag in end_tags:
	    main_text=main_text.replace(end_tag,"<br>")
    
    return main_text

def getTitle(soup):
    title=(soup.find("title")).text
    return title


