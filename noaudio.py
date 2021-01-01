from os import error
import subprocess
import os

POSSIBLE_EXTENSIONS = [".avi", ".mp4", "mov"]

directory = input("Give directory path containing video footage. --->")
directory = directory.replace("\\", "/")
print(f"Searching in {directory}.")

if os.path.exists(directory):
    try:
        for files in os.walk(directory):
            for list in files:
                for filename in list:
                    for extension in POSSIBLE_EXTENSIONS:
                        # Lowercase the filename to make the program case insensitive
                        if filename.lower().endswith(extension.lower()):
                            noaudio = "noaudio_" + filename
                            command = 'ffmpeg -i ' + filename + ' -c copy -an ' + noaudio
                            subprocess.call(command, shell=False)
                            print('Done removing audio.')

        print('Progam exiting...')

    except Exception as e:
        print(error, e)
        print('Progam exiting...')

else:
    print("No video footage found, try again with another directory path.")