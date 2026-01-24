import os

from google.genai import types

def get_files_info(working_directory, directory="."):
    try:
        abs_working_dir = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(abs_working_dir, directory))
        valid_target_dir = os.path.commonpath([abs_working_dir, target_dir]) == abs_working_dir
        
        if not valid_target_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        
        is_dir = os.path.isdir(target_dir)
        
        if not is_dir:
            return f'Error: "{directory}" is not a directory'
        
        list_dir = os.listdir(target_dir)
        
        content_dir = []
        
        for content in list_dir:
            file_name = f"- {content}:"
            path = os.path.join(target_dir, content)            
            file_size = f"file_size={os.path.getsize(path)} bytes"
            is_dir = f"is_dir={os.path.isdir(path)}"
            content_dir.append(f"{file_name} {file_size} {is_dir}")
            
        info_content_dir = "\n".join(content_dir)
        
        return info_content_dir
    except Exception as e:
        return f"Error: {e}"
    
schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in a specified directory relative to the working directory, providing file size and directory status",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="Directory path to list files from, relative to the working directory (default is the working directory itself)",
            ),
        },
    ),
)
    