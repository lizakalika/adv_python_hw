import shutil
import os

shutil.unpack_archive('/Users/Elizaveta/Downloads/main', '/Users/Elizaveta/Desktop') #распаковали

folders = []

for current_dir, dirs, files in os.walk('/Users/Elizaveta/Downloads/main'): 
    for i in files:
        if i[-2:] == 'py' and current_dir not in folders:
            folders.append(current_dir)
            
print(sorted(folders,key=str.lower))

