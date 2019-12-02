from django.db import models
from bs4 import BeautifulSoup
import random
from urllib.request import urlopen
import csv
import re

# Create your models here.

def csv_mod_read_row2(path, idx):
    with open(path, 'r',encoding="utf-8") as f:
        reader = csv.reader(f)
        line_num = 0
        while True:
            if line_num == idx:
                return next(reader)
            f.readline()
            line_num += 1
    return None

def random_scrape():
    number=random.randint(2,16772)
    url=csv_mod_read_row2('Book1.csv', number)
    r=urlopen(url[0])
    soup = BeautifulSoup(r,"lxml",from_encoding="shift_jis")
    main_text=(soup.find("div","main_text")).text
    
    endtag=re.compile("\n")
    end_tags=endtag.findall(main_text)
    for end_tag in end_tags:
	    main_text=main_text.replace(end_tag,"<br>")
    r.close()
    return main_text