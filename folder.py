
from bs4 import BeautifulSoup
import requests

def bytes_parser(data_units, unit_name):
    if unit_name == 'KB':
        return data_units * 1024
    if unit_name == 'MB':
        return data_units * 1024 * 1024
    return data_units

def file_type_parser(file_name):
    names = file_name.split('.')
    if (len(names) == 1) or (names[0] == ''):
        return '<outros>'
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
            self.lines = int(span_data[0])
            
            data_units = float(span_data[4])
            unit_name = span_data[5]
            
            self.size_in_bytes = int(bytes_parser(data_units, unit_name))
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
  
    def get_tree(self, tabsize=0):
        lines = []
        if self.type == "file":
            lines.append(
              ("|   "*(tabsize -1)) + "|___" +
              self.name +
              " (lines:" + str(self.lines) +
              ", Bytes:" + str(self.size_in_bytes) +
              ")"
            )
        if self.type == "folder":
            lines.append("|   "*tabsize + "[" + self.name + "]")
            for e in self.elements:
                lines += e.get_tree(tabsize + 1)
        return lines
    
    def get_resume(self):
        if self.type == "file":
            return {
                self.file_type : {
                    "lines": self.lines,
                    "bytes": self.size_in_bytes
                }
            }
        if self.type == "folder":
            element_resume = {}
            children_elements_types = [e.get_resume() for e in self.elements]
            for child_element_types in children_elements_types:
                for element_type in child_element_types:
                    lines = child_element_types[element_type]['lines']
                    byte_size = child_element_types[element_type]['bytes']
                    if element_type in element_resume.keys():
                        element_resume[element_type]['lines'] += lines
                        element_resume[element_type]['bytes'] += byte_size
                    else:
                        element_resume[element_type] = {
                            'lines': lines,
                            'bytes': byte_size
                        }
            return element_resume