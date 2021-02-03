from bs4 import BeautifulSoup
from main_folder import MainFolder
import requests
from multiprocessing import Pool
import os

def create_folder(repository):
    lines = MainFolder(repository).to_str()
    for line in lines:
        print(line)

script_dir = os.path.dirname(__file__)
rel_path = "repositories.txt"
abs_file_path = os.path.join(script_dir, rel_path)


filehandle = open(abs_file_path)
filevalue = filehandle.read()
repositories = filevalue.split('\n')
print(repositories)

pool = Pool()
result = pool.map(create_folder, repositories)