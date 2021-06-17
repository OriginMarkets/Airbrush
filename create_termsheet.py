"""
create_termsheet is a command line tool that can be used to render
a termsheet based on the Origin termsheet template and a json file
based on the Airbrush data standard

Usage:
    python create_termsheet.py <json_input_file> <docx_output_file>

Args:
    <json_input_file> is the path to a json file in Airbrush format
    <docx_output_file> is the path to the rendered termsheet to create
"""
import argparse
from pathlib import Path
import json
from docxtpl import DocxTemplate

BASE_DIR = Path(__file__).parent
TERMSHEET_TEMPLATE_PATH = BASE_DIR / "Machine-Readable Termsheet.docx"

ARGNAME_INPUT_JSON_PATH = "json_input_file"
ARGNAME_OUTPUT_DOCX_PATH = "docx_output_file"


def validate_file_type(parser, file_path, ext, must_exist=True):
    """
    Validates file path string passed to an argparse parser. Checks that string has a valid
    extension and is a file that exists if must_exist = True. Raises validation errors
    if any of the conditions fail.

    Args:
        parser: An argparse.ArgumentParser instance used to raise validation errors
        file_path: The file path string to be validated
        ext: The file extenion to validate the file path against. In the format '.*'
        must_exist: Boolean for whether to check existence of file in validation. Defaults to True

    Returns:
        str | None: The string passed to it if its valid, otherwise None
    """
    path = Path(file_path)
    if must_exist and not (path.exists() and path.is_file):
        parser.error(f"The file {file_path} does not exist")
    elif not path.suffix == ext:
        parser.error(f"The file {file_path} has the wrong extension. Expected {ext}")
    return file_path


def create_arg_parser():
    """
    Creates an argument parser to be used when the file is run directly as a command line tool.

    Returns:
        argparse.ArgumentParser: A parser to be used to parse arguments from sys.argv
    """
    DESCRIPTION = (
        "A command line tool to create a termsheet using "
        "the Origin termsheet template with an Airbrush-compliant "
        "json file"
    )
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument(
        ARGNAME_INPUT_JSON_PATH,
        type=lambda f: validate_file_type(parser, f, ".json"),
        help="The path to the json input file",
    )
    parser.add_argument(
        ARGNAME_OUTPUT_DOCX_PATH,
        type=lambda f: validate_file_type(parser, f, ".docx", must_exist=False),
        help="The path to create the docx termsheet at",
    )
    return parser


def create_termsheet(input_file_path, output_file_path):
    """
    Create a termsheet in docx format using the Origin template and a json input file.

    Args:
        input_file_path: A json input file path to render the termsheet with
        output_file_path: A docx output file path to write to on success
    """
    with open(input_file_path, "r") as f:
        termsheet_fields = json.load(f)

    termsheet_template = DocxTemplate(TERMSHEET_TEMPLATE_PATH)
    termsheet_template.render(termsheet_fields)
    termsheet_template.save(output_file_path)


if __name__ == "__main__":
    parser = create_arg_parser()
    args = vars(parser.parse_args())

    termsheet_data_file = args[ARGNAME_INPUT_JSON_PATH]
    termsheet_output_file = args[ARGNAME_OUTPUT_DOCX_PATH]

    create_termsheet(termsheet_data_file, termsheet_output_file)
    print(f"Successfully created new termsheet: {termsheet_output_file}")
