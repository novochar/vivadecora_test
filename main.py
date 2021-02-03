from bs4 import BeautifulSoup
from main_folder import MainFolder
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

def write_repository_states(repository_name):
    folder_root = MainFolder(repository_name)
    repository_path = "output/" + repository_name
    if not os.path.exists(os.path.dirname(repository_path)):
        try:
            os.makedirs(os.path.dirname(repository_path))
        except OSError as exc:
            if exc.errno != errno.EEXIST:
                raise

    tree_text = folder_root.get_tree_str()
    resume_text = folder_root.get_resume_str()

    ftree = open(repository_path + ".tree.txt", "w")
    ftree.write(tree_text)
    ftree.close()

    fresume = open(repository_path + ".resume.txt", "w")
    fresume.write(resume_text)
    fresume.close()

def create_folder(repository_name):
    print("processando: " + repository_name)
    write_repository_states(repository_name)
    print("salvo: " + repository_name)


def main():
    repositories = read_repositories()

    pool = Pool()
    pool.map(create_folder, repositories)
    print('Execução encerrada com sucesso')

if __name__ == "__main__":
    main()