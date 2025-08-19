import os

def findFilesWithEnding(folder_path, fileEnding):
    return [f[:-4] for f in os.listdir(folder_path) if f.endswith(fileEnding)]