
from bs4 import BeautifulSoup
import requests
from multiprocessing import Pool

def bytes_parser(data_units, unit_name):
  if unit_name == 'KB':
    return data_units * 1024
  if unit_name == 'MB':
    return data_units * 1024 * 1024
  return data_units

def file_type_parser(file_name):
  names = file_name.split('.')
  if (len(names) == 1) or (names[0] == ''):
    return 'outros'
  return names[-1]

class Folder:
  def __init__(self, repositorie_url, name):
    self.name = name
    self.repositorie_url = repositorie_url
    html = requests.get("https://github.com/" + repositorie_url).content
    soup = BeautifulSoup(html, 'html.parser')
    result = soup.find_all('div', role='rowheader')
    
    span = soup.find( 'span', { "class": "file-info-divider" })
    if span:
      self.type = 'file'
      self.file_type = file_type_parser(name)
      span_data = span.find_parent('div').text.replace('\n', '').split()
      self.lines = span_data[0]
      
      data_units = float(span_data[4])
      unit_name = span_data[5]
      
      self.byte_size = int(bytes_parser(data_units, unit_name))
      print(self.file_type)
      print(self.byte_size)
      print(span_data)
    else:
      self.type = 'folder'
      self.elements = [x for x in [ self.element_parse(i) for i in result] if x is not None]
    
  def element_parse(self, element):
    element_link = element.find('a', href=True, title=True)
    href = element_link['href']
    if element_link['title'] == "Go to parent directory":
      return None
    else:
      return Folder(href, element_link['title'])
  
  def to_str(self, tabsize=0):
    lines = []
    if self.type == 'file':
      lines.append(
        ("|   "*(tabsize -1)) + "|___" +
        self.name +
        ' lines:' + str(self.lines) +
        ", Bytes:" + str(self.byte_size)
      )
    if self.type == 'folder':
      lines.append("|   "*tabsize + self.name)
      for e in self.elements:
        lines += e.to_str(tabsize + 1)
    return lines
