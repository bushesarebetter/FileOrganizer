# FileOrganizer
File organizer/disorganizer for folders, built in python and compiled through pyinstaller

## Running organize/disorganize

### Windows
1. Download the .exe files from the ```dist/``` folder
2. Now, just run like a normal .exe (Preferably through command line with ```./organize.exe``` or ```./disorganize.exe```

### Mac
1. Install pyinstaller with
   ```pip3 install pyinstaller```
2. Download the source files (You can download the full repo or just the individual .py files). Please note that you may have to delete the ```.spec``` files for pyinstaller to properly compile, I'm not sure how it works on mac.
4. You will probably have to change ```common_dir_names``` in ```organize.py```. Change the listing of .exe to .app so it can correctly identify executables on your platform
5. Run ```pyinstaller --onefile organize.py``` for the organizer and ```pyinstaller --onefile disorganize.py``` for the disorganizer

### How it works
After you run the .py/.exe/.whatever file, it will ask you what folder to organize/disorganize. For ```disorganize.exe```, it is highly recommended that you only use it on folders that have been organized by ```organize.exe```, as otherwise it will unpack all the files from folders and trying to reorganize with ```organize.exe``` won't work (e.g. you have specific documents for different companies, then disorganizing will take out all the documents but won't save the original folders so when you reorganize, it'll only organize into the directories you specified, such as Folders, Executables, etc"

## IMPORTANT

To modify how directories are sorted in ```organize.py```, simply go over to the ```common_dir_names``` directory and add any listing you want, e.g.
```'.csv': 'Spreadsheets'```. 
Then, add the directory specified (e.g. ```'Spreadsheets'```) to the ```possible_orgs``` folder (You may notice that ```'Folders'``` is also in the ```possible_orgs``` array, keep it there). 
Finally, recompile with ```pip3 install pyinstaller```, and then ```pyinstaller --onefile organize.py``` and ```pyinstaller --onefile disorganize.py``` (if you made any changes). The executables will be outputted in the ```dist/``` folder.

### Another note for recompiling
```pyinstaller``` will probably make another folder called ```build```, that's fine, it just has some build info and stuff that isn't important, but the executables are still put into the ```dist/``` folder.
