import os

def get_files_info(working_directory, directory="."):
    try:
        abs_path_work_dir = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(abs_path_work_dir, directory))
        valid_target_dir = os.path.commonpath([abs_path_work_dir, target_dir]) == abs_path_work_dir
        
        if not valid_target_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        
        is_dir = os.path.isdir(target_dir)
        
        if not is_dir:
            return f'Error: "{directory}" is not a directory'
        
        list_dir = os.listdir(target_dir)
        
        content_dir = []
        
        for file in list_dir:
            file_name = f"- {file}:"
            path = os.path.join(target_dir, file)            
            file_size = f"file_size={os.path.getsize(path)} bytes"
            is_dir = f"is_dir={os.path.isdir(path)}"
            content_dir.append(f"{file_name} {file_size} {is_dir}")
            
        info_content_dir = "\n".join(content_dir)
        
        return info_content_dir
    except Exception as e:
        return f"Error: {e}"
    