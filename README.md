# AWS::IAM::Role Policy Parser
## Installation
> git clone https://github.com/Griger5/AWS_IAM_Role_Policy_Parser.git

The program makes use of only the standard libraries, so no further requirements besides Python 3.x are required.

## Usage
To use the parser in your code:
>import aws_iam_parser
>
>parser = aws_iam_parser.Parser()

To run the tests:
>python3 unit_tests.py

## Functions
#### Parser.verify_resource( _json_ )
##### Parameters: <br>json: File path to a JSON file or a dictionary containing JSON data 
The parser's main function is verifying the given JSON's 'Resource' field.
If the 'Resource' field is only a single asterisk, the method returns False, otherwise it returns True.
Returns None and prints an error message when the method encounters an error.
Example use:
>parser = aws_iam_parser.Parser()
>path = "path/to/file.json"
>result = parser.verify_resource(path)

#### Parser.load_file_path( _path_ )
##### Parameters: <br>path: type => string. File path to a JSON file.
Loads a JSON file from the given path. Returns the JSON file as a dictionary on success, returns None and prints an error message on failure.
Example use:
>parser = aws_iam_parser.Parser()
>path = "path/to/file.json"
>data = parser.load_file_path(path)