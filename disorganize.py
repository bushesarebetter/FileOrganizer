# Unfolderify all the folders in set directory and set it to be just one dir
import os

print("File disorganizer for any folder, takes all the files/folders out of the base level path and moves them out, then deletes the folder they were originally in")
print("What folder would you like to disorganize? (Make sure to input the right one otherwise all your files might get yeeted into a folder)")

folder_to_look_at = input()
folders = [f for f in os.listdir(folder_to_look_at) if f != 'desktop.ini']

for folder in folders:
    try:
        files = os.listdir(f"{folder_to_look_at}\\{folder}")
        for file in files:
            os.rename(f"{folder_to_look_at}\\{folder}\\{file}", f"{folder_to_look_at}\\{file}")
        os.rmdir(f"{folder_to_look_at}\\{folder}")
    except:
        pass # Safety for if os cant move into the dir (assuming its a regular file)