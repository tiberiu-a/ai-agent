import os
import subprocess

def run_python_file(working_directory, file_path, args=None):
    try:
        abs_path_work_dir = os.path.abspath(working_directory)
        abs_file_path = os.path.normpath(os.path.join(abs_path_work_dir, file_path))
        valid_target_dir = os.path.commonpath([abs_path_work_dir, abs_file_path]) == abs_path_work_dir
        
        if not valid_target_dir:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        
        is_file = os.path.isfile(abs_file_path)
        
        if not is_file:
            return f'Error: "{file_path}" does not exist or is not a regular file'
        
        if not file_path.endswith('.py'):
            return f'Error: "{file_path}" is not a Python file'
        
        command = ["python", abs_file_path]
        
        if args:
            command.extend(args)
            
        completed_run = subprocess.run(args=command, capture_output=True, text=True, timeout=30)
        
        return_code = completed_run.returncode
        stdout = completed_run.stdout
        stderr = completed_run.stderr
        output_str = ''
        
        if return_code != 0:
            output_str += f"Process exited with code {return_code}"
        
        if stdout:
            output_str += f"STDOUT: {stdout}"
            
        if stderr:
            output_str += f"STDERR: {stderr}"
            
        if not stdout or not stderr:
            output_str += "No output produced"
            
        return output_str        
        
    except Exception as e:
        return f"Error: executing Python file: {e}"
    
run_python_file("calculator", "main.py")
    
    