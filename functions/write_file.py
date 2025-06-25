import os

def write_file(working_directory, file_path, content):
    try:
        abs_path = os.path.abspath(working_directory)
        joined_file_path = os.path.abspath(os.path.join(abs_path, file_path))

        if (not joined_file_path.startswith(abs_path)):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        if (not os.path.exists(os.path.dirname(joined_file_path))):
            os.makedirs(os.path.dirname(joined_file_path))

        with open(joined_file_path, "w") as f:
            f.write(content)
        
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as err:
        return f"Error: {err}"
