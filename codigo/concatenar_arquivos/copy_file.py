import os
import shutil

path = os.path.abspath(os.path.dirname(os.path.curdir))
path_abs = os.path.join(path, 'files')

files = []
for file in os.listdir(path_abs):
    file_path = os.path.join(path_abs, file)
    if os.path.isfile(file_path):
        files.append(file)

files.sort()
files.reverse()

os.mkdir(os.path.join(path_abs, 'resultado'))
shutil.copy(os.path.join(path_abs, files[0]), os.path.join(path_abs, 'resultado'))
