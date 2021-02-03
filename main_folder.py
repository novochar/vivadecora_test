from folder import Folder

def file_types_parser(file_types):
    total_lines = 0
    total_bytes = 0
    for i in file_types:
        total_lines += file_types[i]['lines']
        total_bytes += file_types[i]['bytes']
    total_resume = {}
    for i in file_types:
        total_resume[i] = {
            "lines": file_types[i]['lines'] / total_lines * 100.0,
            "bytes": file_types[i]['bytes'] / total_bytes * 100.0
        }
    
    string_list = ["Extensão   |     Linhas     |    Bytes"]
    for i in file_types:
        string_list.append(
            "%10s |%10i(%2.0f%%) |%10i(%2.0f%%)" %
            (
                i,
                file_types[i]['lines'],
                total_resume[i]['lines'],
                file_types[i]['bytes'],
                total_resume[i]['bytes']
            )
        )
    return "\n".join(string_list)


class MainFolder(Folder):
    def __init__(self, project_name):
        super().__init__(project_name, "Projeto " + project_name)

    def get_resume_str(self):
       return file_types_parser(self.get_resume())

    def get_tree_str(self):
        return "\n".join(super().get_tree())

 