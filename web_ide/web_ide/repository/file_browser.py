# Think of how to display empty folder since it will have no children inside and
# could be treated as file.
import os
import base64


class FileBrowser(object):
    GIT_FOLDER = '.git'
    TMP_FOLDER = '/tmp'
    TYPE_FOLDER = 'folder'
    TYPE_FILE = 'file'

    def __init__(self, base_dir):
        self.base_dir = base_dir
        self.base_name = os.path.basename(base_dir)

    def get_structure(self):
        structure = []

        for root, dirs, files in os.walk(self.base_dir):
            if self.GIT_FOLDER in root:
                continue

            cut_path = self.cut_path_to_base_dir(self.base_name, root)
            parent_directory = self.find_parent_directory_by_id(structure, cut_path)

            if parent_directory:
                append_to = parent_directory['children']
            else:
                append_to = structure

            for d in dirs:
                if self.GIT_FOLDER in d:
                    continue

                d_cut_path = self.cut_path_to_base_dir(self.base_name, os.path.join(root, d))
                append_to.append({'label': d, 'id': d_cut_path, 'children': []})

            for f in files:
                f_cut_path = self.cut_path_to_base_dir(self.base_name, os.path.join(root, f))
                append_to.append({'label': f, 'id': f_cut_path})

        return structure

    def create_new_entity(self, path, entity_type):
        if entity_type == self.TYPE_FOLDER:
            self._create_new_folder(path)
        elif entity_type == self.TYPE_FILE:
            self._create_new_file(path)

    def _create_new_folder(self, folder_path):
        os.makedirs(os.path.join(self.TMP_FOLDER, folder_path))

    def _create_new_file(self, file_path):
        pass

    @classmethod
    def get_content_base_64(cls, temp_path):
        real_path = os.path.join(cls.TMP_FOLDER, temp_path)
        with open(real_path, 'rb') as fb:
            content = fb.read()
            return base64.b64encode(content)

    @staticmethod
    def find_parent_directory_by_id(parent, id):
        for obj in parent:
            if obj['id'] == id:
                return obj
            elif obj.get('children'):
                found = FileBrowser.find_parent_directory_by_id(obj['children'], id)
                if found:
                    return found

    @staticmethod
    def cut_path_to_base_dir(base_dir, path):
        spl = path.split('/')
        base_dir_index = spl.index(base_dir)
        return '/'.join(spl[base_dir_index:])
