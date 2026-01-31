import os

from google.genai import types

def write_file(working_directory, file_path, content):
    try:
        abs_path_work_dir = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(abs_path_work_dir, file_path))
        valid_target_dir = os.path.commonpath([abs_path_work_dir, target_file]) == abs_path_work_dir
        
        if not valid_target_dir:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        
        is_dir = os.path.isdir(target_file)        
        
        if is_dir:
            return f'Error: Cannot write to "{file_path}" as it is a directory'
        
        os.makedirs(abs_path_work_dir, exist_ok=True)
        
        with open(target_file, "w") as f:
            f.write(content)
            
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: {e}"

# write_file(working_directory, file_path, content)
    
schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Overwrites an existing file or writes to a new file if it doesn't exist (and creates required dirs safely), constrained to the currently working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file to write.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to write to the file as a string",
                
            )
        },
    ),
)