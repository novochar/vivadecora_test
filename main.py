from bs4 import BeautifulSoup
from main_folder import MainFolder
import requests
from multiprocessing import Pool
import os
import errno

def read_repositories():
    script_dir = os.path.dirname(__file__)
    rel_path = "repositories.txt"
    abs_file_path = os.path.join(script_dir, rel_path)

    filehandle = open(abs_file_path)
    filevalue = filehandle.read()
    return filevalue.split('\n')

def write_repository_state(repository_name, tree_text, resume_text):
    repository_path = "output/" + repository_name
    if not os.path.exists(os.path.dirname(repository_path)):
        try:
            os.makedirs(os.path.dirname(repository_path))
        except OSError as exc:
            if exc.errno != errno.EEXIST:
                raise
    ftree = open(repository_path + ".tree.txt", "w")
    ftree.write(tree_text)
    ftree.close()

    fresume = open(repository_path + ".resume.txt", "w")
    fresume.write(resume_text)
    fresume.close()

def create_folder(repository_name):
    print("processando: " + repository_name)
    main_folder = MainFolder(repository_name)
    repository_tree_string = "\n".join(main_folder.to_str())
    repository_resume_string = main_folder.get_file_types()
    write_repository_state(repository_name, repository_tree_string, repository_resume_string )
    print("salvo: " + repository_name)


def main():
    repositories = read_repositories()

    pool = Pool()
    pool.map(create_folder, repositories)
    print('Execução encerrada com sucesso')

if __name__ == "__main__":
    main()