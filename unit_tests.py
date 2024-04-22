import unittest
from pathlib import Path

from aws_iam_parser import Parser

class FileLoadTests(unittest.TestCase):
    def test_loading_json_from_path(self):
        parser = Parser()
        root_dir = Path(__file__).resolve().parent
        file_path = str(root_dir)+"\\test_data\\valid_resource.json"

        data = parser.load_file_path(file_path)

        self.assertIsInstance(data, dict)

    def test_loading_not_json_from_path(self):
        parser = Parser()
        root_dir = Path(__file__).resolve().parent
        file_path = str(root_dir)+"\\test_data\\not_a_json.txt"

        data = parser.load_file_path(file_path)

        self.assertIsNone(data)
    
    def test_loading_json_from_wrong_path(self):
        parser = Parser()
        root_dir = Path(__file__).resolve().parent
        file_path = str(root_dir)+"\\test_data\\invalid_resource.json"

        data = parser.load_file_path(file_path)

        self.assertIsNone(data)


class CheckAsteriskTests(unittest.TestCase):
    def test_single_asterisk(self):
        parser = Parser()
        argument = "*"

        result = parser.check_single_asterisk(argument)

        self.assertFalse(result)

    def test_double_asterisk(self):
        parser = Parser()
        argument = "**"

        result = parser.check_single_asterisk(argument)

        self.assertTrue(result)

    def test_string(self):
        parser = Parser()
        argument = "Lorem Ipsum"

        result = parser.check_single_asterisk(argument)

        self.assertTrue(result)

    def test_string_asterisk_at_start(self):
        parser = Parser()
        argument = "*Lorem Ipsum"

        result = parser.check_single_asterisk(argument)

        self.assertTrue(result)


class VerifyResourceTests(unittest.TestCase):
    def test_valid_resource(self):
        parser = Parser()
        root_dir = Path(__file__).resolve().parent
        file_path = str(root_dir)+"\\test_data\\valid_resource.json"

        result = parser.verify_resource(file_path)

        self.assertTrue(result)

    def test_single_asterisk(self):
        parser = Parser()
        root_dir = Path(__file__).resolve().parent
        file_path = str(root_dir)+"\\test_data\\1asterisk.json"

        result = parser.verify_resource(file_path)

        self.assertFalse(result)

    def test_double_asterisk(self):
        parser = Parser()
        root_dir = Path(__file__).resolve().parent
        file_path = str(root_dir)+"\\test_data\\2asterisk.json"

        result = parser.verify_resource(file_path)

        self.assertTrue(result)

    def test_wrong_format(self):
        parser = Parser()
        root_dir = Path(__file__).resolve().parent
        file_path = str(root_dir)+"\\test_data\\wrong_format.json"

        result = parser.verify_resource(file_path)

        self.assertIsNone(result)

    def test_not_a_json(self):
        parser = Parser()
        root_dir = Path(__file__).resolve().parent
        file_path = str(root_dir)+"\\test_data\\not_a_json.txt"

        result = parser.verify_resource(file_path)

        self.assertIsNone(result)

    def test_wrong_path(self):
        parser = Parser()
        root_dir = Path(__file__).resolve().parent
        file_path = str(root_dir)+"\\test_data\\invalid_resource.json"

        result = parser.verify_resource(file_path)

        self.assertIsNone(result)

    def test_data_valid(self):
        parser = Parser()
        data = {'PolicyName': 'root', 'PolicyDocument': {'Version': '2012-10-17', 'Statement': [{'Sid': 'IamListAccess', 'Effect': 'Allow', 'Action': ['iam:ListRoles', 'iam:ListUsers'], 'Resource': 'This is a valid resource'}]}}

        result = parser.verify_resource(data)

        self.assertTrue(result)

    def test_data_not_valid(self):
        parser = Parser()
        data = {'PolicyName': 'root', 'PolicyDocument': {'Version': '2012-10-17', 'Statement': [{'Sid': 'IamListAccess', 'Effect': 'Allow', 'Action': ['iam:ListRoles', 'iam:ListUsers'], 'Resource': '*'}]}}

        result = parser.verify_resource(data)

        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()