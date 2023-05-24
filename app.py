import os

def rename_files(folder_path, text_to_remove):
    # Get a list of all files in the folder
    files = os.listdir(folder_path)
    
    # Iterate over each file
    for file_name in files:
        if file_name.endswith(".mp3"):
            # Construct the new file name by removing the specified text
            new_file_name = file_name.replace(text_to_remove, "")
            
            # Get the full paths of the old and new file names
            old_file_path = os.path.join(folder_path, file_name)
            new_file_path = os.path.join(folder_path, new_file_name)
            
            try:
                # Rename the file
                os.rename(old_file_path, new_file_path)
                print(f"Renamed: {file_name} -> {new_file_name}")
            except Exception as e:
                print(f"Error renaming {file_name}: {str(e)}")

# Example usage
folder_path = str(input("Input folder location: "))
text_to_remove = str(input("String to remove: "))

rename_files(folder_path, text_to_remove)
