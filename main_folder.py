from folder import Folder

class MainFolder(Folder):
    def __init__(self, project_name):
        super().__init__(project_name, project_name)