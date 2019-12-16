import os
import sys
import logging

ROOTPATH=os.path.dirname(__file__)
EGGSPATH=os.path.join(ROOTPATH,'eggs')
print(os.listdir(EGGSPATH))
for egg in os.listdir(EGGSPATH):
    sys.path.append(os.path.join(EGGSPATH,egg))
