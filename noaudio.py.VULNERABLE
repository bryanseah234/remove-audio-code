from os import error
import subprocess
import os

POSSIBLE_EXTENSIONS = ["avi", "mp4", "mov"]

#MAKE SURE DIRECTORY DOES NOT HAVE SPACES
directory = input("Give directory path containing video footage: ")
directory = directory.replace("\\", "/")
print(f"Searching in {directory}")

if os.path.exists(directory):
    try:
        for files in os.walk(directory):
            for l in files:
                for filename in l:
                    if '.' in filename:
                        ext = filename.split('.')[1]
                        print(ext)
                        if ext.lower() in POSSIBLE_EXTENSIONS:
                            noaudio = "noaudio_" + filename
                            oldpath = os.path.join(directory, filename)
                            newpath = path = os.path.join(directory, noaudio)
                            command = 'ffmpeg -i ' + oldpath + ' -c copy -an ' + newpath
                            subprocess.call(command, shell=True)
                            print('Removed audio')

        print('Done, exiting')

    except Exception as e:
        print(error, e)
        print('Error, exiting')

else:
    print("No video footage found, try again with another directory path.")
