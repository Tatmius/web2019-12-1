from django.db import models
from bs4 import BeautifulSoup
import random
from urllib.request import urlopen
import csv

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


number=random.randint(2,16772)
print(number)
#url=urlopen('http://pubserver2.herokuapp.com/api/v0.1/books/{}/content'.format(book_id))
url=csv_mod_read_row2('Book1.csv', number)
print(url)
r=urlopen(url[0])
soup = BeautifulSoup(r,"lxml",from_encoding="shift_jis")
#main_text=soup.find("div","main_text")
r.close()