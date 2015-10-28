# Think of how to display empty folder since it will have no children inside and
# could be treated as file.
import os


class FileBrowser(object):
    def __init__(self, base_dir):
        self.base_dir = base_dir
        self.base_name = os.path.basename(base_dir)

    def get_structure(self):
        structure = []

        current_root = None

        for root, dirs, files in os.walk(self.base_dir):

            if root == self.base_dir:
                current_root = structure
            else:
                cut_path = self.cut_path_to_base_dir(self.base_name, root)
                current_root = [obj['children'] for obj in current_root if 'children' in obj
                                and obj['id'] == cut_path][0]

            for d in dirs:
                d_cut_path = self.cut_path_to_base_dir(self.base_name, os.path.join(root, d))
                current_root.append({'label': d, 'id': d_cut_path, 'children': []})

            for f in files:
                f_cut_path = self.cut_path_to_base_dir(self.base_name, os.path.join(root, f))
                current_root.append({'label': f, 'id': f_cut_path})

        return structure

    @staticmethod
    def cut_path_to_base_dir(base_dir, path):
        spl = path.split('/')
        base_dir_index = spl.index(base_dir)

        return '/'.join(spl[base_dir_index:])
