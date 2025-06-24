import os
def get_files_info(working_directory, directory=None):
    try:
        abs_path = os.path.abspath(working_directory)
        joined_path = os.path.abspath(os.path.join(abs_path, directory))
        #print (joined_path)
        #print (os.path.isdir(joined_path))

        if (not os.path.isdir(joined_path)):
            return f'Error: "{directory}" is not a directory'

        if (not joined_path.startswith(abs_path)):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        result = []
        dir_content = os.listdir(joined_path)
        #print(dir_content)
        for item in dir_content:
            item_path = os.path.join(joined_path, item)
            is_dir = os.path.isdir(item_path)
            file_size = os.path.getsize(item_path)


            result.append(f"- {item}: file_size={file_size}, is_dir={is_dir}")

        #print (os.path.abspath(working_directory))
        #print (os.path.join(working_directory, directory))
        #print (os.path.isdir(working_directory))
        #print (os.listdir(working_directory))
        return "\n".join(result)
    except Exception as err:
        return f"Error: {err}"
