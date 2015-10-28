import os
from unittest import TestCase

from web_ide.repository.file_browser import FileBrowser


class FileBrowserTest(TestCase):
    def setUp(self):
        self.test_folder = os.path.join(os.path.dirname(__file__), 'file_browser_test_folder')

    def test_file_browser(self):
        file_browser = FileBrowser(self.test_folder)

        expected_structure = [
            {'label': 'directory_1', 'id': 'file_browser_test_folder/directory_1', 'children': [
                {'label': 'file_1', 'id': 'file_browser_test_folder/directory_1/file_1'}
            ]},
            {'label': 'file_1', 'id': 'file_browser_test_folder/file_1'},
            {'label': 'file_2', 'id': 'file_browser_test_folder/file_2'}
        ]

        actual_structure = file_browser.get_structure()

        self.assertEqual(actual_structure, expected_structure)

    def test_cut_path_to_base_dir(self):
        base_dir = 'base_dir'
        path = '/opt/vagrant/base_dir/project/file.txt'
        expected_path = 'base_dir/project/file.txt'

        actual_path = FileBrowser.cut_path_to_base_dir(base_dir, path)

        self.assertEqual(actual_path, expected_path)