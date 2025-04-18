# Manually generate a basic timestamp
def timestamp():
    import time
    return str(int(time.time()))

#Files in the Source Directory
def files_in_directory(path):
    from pathlib import Path
    return [f for f in Path(path).iterdir()]

# Check if File Already Exists
def file_exists(path):
    from pathlib import Path
    return Path(path).exists()

#Copy a File
def copy_file(source_path, dest_path):
    with open(source_path, 'rb') as src_file:
        content = src_file.read()
    with open(dest_path, 'wb') as dest_file:
        dest_file.write(content)

# Ask user for source and destination folders
source_dir = input("Enter the source directory path: ")
dest_dir = input("Enter the destination directory path: ")

files = files_in_directory(source_dir)

#Backup Process
for file in files:
        file_name = file.name
        source_file_path = str(file)
        dest_file_path = f"{dest_dir}/{file_name}"

        # If file exists, append a basic timestamp
        if file_exists(dest_file_path):
            timestamp = timestamp()
            name_parts = file_name.split('.')
            if len(name_parts) > 1:
                new_name = f"{'.'.join(name_parts[:-1])}_{timestamp}.{name_parts[-1]}"
            else:
                new_name = f"{file_name}_{timestamp}"
            dest_file_path = f"{dest_dir}/{new_name}"

        copy_file(source_file_path, dest_file_path)
        print(f"Copied: {file_name} ➜ {dest_file_path}")