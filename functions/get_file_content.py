import os

from config import MAX_CHARS
from google.genai import types


def get_file_content(working_directory, file_path):
    try:
        abs_path_work_dir = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(abs_path_work_dir, file_path))
        valid_target_dir = os.path.commonpath([abs_path_work_dir, target_dir]) == abs_path_work_dir
        
        if not valid_target_dir:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        
        is_file = os.path.isfile(target_dir)
        
        if not is_file:
            return f'Error: File not found or is not a regular file: "{file_path}"'
        
        with open(target_dir, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            if f.read(1):
                file_content_string += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'

        return file_content_string
    except Exception as e:
        return f"Error: {e}"
    
schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Read a file content relative to the working directory and return its contents as a string, truncated at the configured max characters.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file to read, relative to the working directory.",
            ),
        },
    ),
)