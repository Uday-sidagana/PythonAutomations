import os

from dotenv import load_dotenv
import requests

load_dotenv()

def folder():
   
    directory= input("Directory Format: /Users/macbookair/Desktop/python/AutomationPython/AutomateGithubRepo/ ")
    os.mkdir(directory)
    
