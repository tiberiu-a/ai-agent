import os

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