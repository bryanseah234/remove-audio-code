from os import error
import subprocess
import os

directory = input("Give directory path containing video footage. --->")
directory = directory.replace("\\", "/")
print(f"Searching in {directory}.")

if os.path.exists(directory):
    try:
        for files in os.walk(directory):
            for list in files:
                for filename in list:

                    if filename.endswith(".mov"):
                        noaudio = "noaudio_" + filename
                        command = 'ffmpeg -i ' + filename + ' -c copy -an ' + noaudio
                        subprocess.call(command, shell=False)
                        print('Done removing audio.')

                    elif filename.endswith(".avi"):
                        noaudio = "noaudio_" + filename
                        command = 'ffmpeg -i ' + filename + ' -c copy -an ' + noaudio
                        subprocess.call(command, shell=False)
                        print('Done removing audio.')

                    elif filename.endswith(".mp4"):
                        noaudio = "noaudio_" + filename
                        command = 'ffmpeg -i ' + filename + ' -c copy -an ' + noaudio
                        subprocess.call(command, shell=False)
                        print('Done removing audio.')

                    elif filename.endswith(".MP4"):
                        noaudio = "noaudio_" + filename
                        command = 'ffmpeg -i ' + filename + ' -c copy -an ' + noaudio
                        subprocess.call(command, shell=False)
                        print('Done removing audio.')

                    elif filename.endswith(".MOV"):
                        noaudio = "noaudio_" + filename
                        command = 'ffmpeg -i ' + filename + ' -c copy -an ' + noaudio
                        subprocess.call(command, shell=False)
                        print('Done removing audio.')

                    elif filename.endswith(".AVI"):
                        noaudio = "noaudio_" + filename
                        command = 'ffmpeg -i ' + filename + ' -c copy -an ' + noaudio
                        subprocess.call(command, shell=False)
                        print('Done removing audio.')

        print('Progam exiting...')

    except:
        print(error)
        print('Progam exiting...')

else:
    print("No video footage found, try again with another directory path.")