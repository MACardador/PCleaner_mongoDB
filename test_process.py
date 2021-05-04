import os.path
import unittest
from unittest.mock import patch

import jsonpickle

import process
from dto import folder


class TestProcess(unittest.TestCase):

    def test_recursive_folder(self):
        with patch('os.listdir') as mocked_listdir:
            with patch('os.path.isdir') as mocked_isdir:
                mocked_listdir.return_value = ["Photos.jpeg"]
                mocked_isdir.side_effect = [False]
                directory = "C:\\some\\folder"
                folders = set()
                process.recursive_folder(directory, folders)
                self.assertTrue(len(folders) == 1)

    def test_get_folders(self):
        with patch('process.get_drives') as mocked_drives:
            with patch('os.listdir') as mocked_listdir:
                with patch('os.path.isdir') as mocked_isdir:
                    mocked_listdir.return_value = ["Photos.jpeg"]
                    mocked_isdir.side_effect = [False]
                    mocked_drives.return_value = ["C:\\"]

                    result = process.get_folders()
                    decoded = jsonpickle.decode(result)
            [print(u) for u in decoded]
            self.assertEqual(folder.Folder("C:\\").directory, next(iter(decoded)).directory)


if __name__ == '__main__':
    unittest.main()
