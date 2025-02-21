import os

print("File organizer for .docx, .exe, .zip, .pdf, .gif, .mp4, .png, .jpeg, .jpg")
print("What folder would you like to organize? (Make sure to input the right one otherwise all your files might get yeeted into a folder)")

folder_to_look_at = input()

# Common file endings for directory sorting
common_dir_names = {
    '.docx': 'Word Documents',
    '.exe': 'Executables',
    '.zip': 'Zipped Folders',
    '.pdf': 'Documents',
    '.gif': "Videos",
    ".mp4": "Videos",
    '.png': "Photos",
    ".jpeg": "Photos",
    ".jpg": "Photos",
}

possible_orgs = ["Word Documents", "Executables", "Zipped Folders", "Documents", "Videos", "Photos", "Folders"]

folders = [f for f in os.listdir(folder_to_look_at) if os.path.isdir(os.path.join(folder_to_look_at, f)) and f not in possible_orgs]


all_files = os.listdir(folder_to_look_at)
for file in all_files:
    if file in folders:
        try: 
            os.mkdir(f"{folder_to_look_at}\\Folders")
        except:
            pass
        os.rename(f"{folder_to_look_at}\\{file}", f"{folder_to_look_at}\\Folders\\{file}")
    else:
        file_ending = file.split('.')[-1]
        file_extension = "." + file_ending

        if file_ending not in possible_orgs and file_extension not in common_dir_names:
            try:
                os.mkdir(f"{folder_to_look_at}\\Misc")
            except:
                pass       
            os.rename(f"{folder_to_look_at}\\{file}", f"{folder_to_look_at}\\Misc\\{file}")
        else:
            try:
                os.mkdir(f"{folder_to_look_at}\\{common_dir_names[file_extension]}")
            except:
                pass
            if file_extension in common_dir_names:
                os.rename(f"{folder_to_look_at}\\{file}", f"{folder_to_look_at}\\{common_dir_names[file_extension]}\\{file}")
        
