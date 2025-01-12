import eyed3
import os
from shutil import copyfile
rootdir = "/mnt/g/musictagttest"
input_path = "input"
output_path = "output"
os.chdir(rootdir)
for item in os.walk("input"):
    for file in item[2]:
        input_file = os.path.join(input_path, file)
        print("Processing file:{}".format(input_file))        
        audiofile=eyed3.load(input_file)
        album = audiofile.tag.album
        output_album_path = os.path.join(output_path, album)
        os.makedirs(output_album_path, exist_ok=True)
        copyfile(os.path.join(input_path, file), os.path.join(output_album_path,  file[2:]))
        
        
        
