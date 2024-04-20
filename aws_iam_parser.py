import json

class Parser():
    """
        Creates a JSON AWS::IAM:Role Policy parser
    """
    def check_single_asterisk(self, arg: str) -> bool:
        """
            Checks if the given argument is a singular asterisk.\n
            Returns False when it is.\n
            Returns True otherwise.
        """
        return False if arg == "*" else True
    def load_file_path(self, path: str) -> dict:
        """
            Loads a JSON file from the given path.\n
            Returns the JSON file as a dictionary on success.\n
            Returns None on failure.
        """
        try:
            with open(path) as file:
                json_file = json.load(file)
            return json_file
        except FileNotFoundError:
            print("JSON file not found")
            return
        except:
            print("Not a JSON file")
            return
    def verify_resource(self, json) -> bool:
        """
            Input can be either a path to the JSON file as a string or a dictionary containing the JSON.\n
            Verifies the contents of the \'Resoure\' field.\n
            Returns False if the field contains a singular asterisk, otherwise returns True.\n
            Returns None if the JSON file appears to be of a different format than AWS:IAM:Role Policy.
        """
        if type(json) == str:
            json = self.load_file_path(json)
        try:
            verification = self.check_single_asterisk(json['PolicyDocument']['Statement'][0]['Resource'])
            return verification
        except:
            print("Wrong JSON format")
            return