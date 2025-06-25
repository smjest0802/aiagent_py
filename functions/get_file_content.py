import os
def get_file_content(working_directory, file_path):
    try:
        abs_path = os.path.abspath(working_directory)
        joined_file_path = os.path.abspath(os.path.join(abs_path, file_path))
        #print (joined_path)
        #print (os.path.isdir(joined_path))

        if (not os.path.isfile(joined_file_path)):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        if (not joined_file_path.startswith(abs_path)):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        MAX_CHARS = 10000

        with open(joined_file_path, "r") as f:
            file_content_string = f.read(MAX_CHARS + 1) # get one more to see if its too big

        print (f"file size is {len(file_content_string)}")

        if len(file_content_string) - 1 == MAX_CHARS:
            file_content_string = file_content_string[:-1] + f'[...File "{file_path}" truncated at 10000 characters]'

        return file_content_string

    except Exception as err:
        return f"Error: {err}"
