import os
import shutil
import sys



def directory(file_extension : str):
	if not file_extension:
		return

	folder_by_extension = {
		"exe": "Software",
		"txt": "Texts",
		"pdf": "PDF Documents",
		"epub": "Books",
		"jpg": "Images",
		"jpeg": "Images",
		"png": "Images",
		"raw": "Images",
		"mp3": "Music",
		"mp4": "Videos",
		"mkv": "Videos",
		"xlsx": "Excel Files",
		"ppt": "Slides",
		"doc": "Documents",
		"rar": "Compressed Files",
		"zip": "Compressed Files",
		"iso": "Iso Files"
	}

	return folder_by_extension.get(file_extension, 'Extras')

def organizer(path:str):
	if not os.path.exist(path):
		print(f"not found {path} or not exists.")
		return 

	files = os.listdir(path)
	extensions = [os.path.splittext(file)[1].strip(".") for file in files]



print(os.path.isabs(os.getcwd()))
